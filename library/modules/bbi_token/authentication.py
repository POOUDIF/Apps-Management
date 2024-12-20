from datetime import timedelta

from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

# this return left time
from .models import BBIToken
from .settings import custom_settings
from django.contrib.auth.models import User

# token checker if token expired or not
def is_token_expired(token):
    return (token.expires - timezone.now()) < timedelta(seconds=0)


# if token is expired new token will be established
# If token is expired then it will be removed
# and new one with different key will be created
def token_expire_handler(token):
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        token = BBIToken.objects.create(username=token.username)
    return is_expired, token


# ________________________________________________
# DEFAULT_AUTHENTICATION_CLASSES
class BBITokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        try:
            # Remove relation to User
            # token = BBIToken.objects.select_related('user').get(key=key)            
            token = BBIToken.objects.get(key=key)
        except BBIToken.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        userData    = User.objects.get(username = token.username)
        # if not token.user.is_active:
        if not userData.is_active:
            raise AuthenticationFailed("User is not active")

        # is_expired, token = token_expire_handler(token)
        is_expired = is_token_expired(token)
        if is_expired:
            token.delete()
            raise AuthenticationFailed("The Token is expired")

        token.expires = timezone.now() + custom_settings.TOKEN_DURATION
        token.save()

        return userData, token
