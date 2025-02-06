from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models import Q
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from knox.models import AuthToken
from knox.serializers import SignupSerializer
from knox.auth import TokenAuthentication
from knox.settings import knox_settings
import logging


logger = logging.getLogger(__name__)
from django.contrib.auth import authenticate


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            logger.warning("Login attempt without email/password")
            return Response(
                {"error": "Email and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=email, password=password)
        
        if not user:
            logger.warning(f"Failed login attempt for email: {email}")
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token_limit = knox_settings.TOKEN_LIMIT_PER_USER
        if token_limit:
            now = timezone.now()
            tokens = user.auth_token_set.filter(
                Q(expiry__gt=now) | Q(expiry__isnull=True)
            )
            if tokens.count() >= token_limit:
                logger.warning(f"Token limit exceeded for user: {user.email}")
                return Response(
                    {"error": "Maximum tokens exceeded"},
                    status=status.HTTP_403_FORBIDDEN
                )

        instance, token = AuthToken.objects.create(user)
        user_logged_in.send(sender=user.__class__, 
                          request=request, user=user)
        logger.info(f"Successful login for user: {user.email}")

        return Response({
            "user": {
                "email": user.email,
                "username": user.username,
                "role": user.role
            },
            "token": token
        })
        
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            _, token = AuthToken.objects.create(user)
            return Response({
                'user': {
                    'email': user.email,
                    'username': user.username,
                    'role': user.role
                },
                'token': token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        if request._auth:
            request._auth.delete()
            user_logged_out.send(sender=request.user.__class__,
                               request=request, user=request.user)
            logger.info(f"User {request.user.email} logged out successfully")
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        logger.warning("Logout attempt without valid token")
        return Response(
            {"error": "No valid authentication token found"},
            status=status.HTTP_400_BAD_REQUEST
        )

class LogoutAllView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_post_response(self, request):
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        request.user.auth_token_set.all().delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        return self.get_post_response(request)
