from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from library.modules.bbi_token.authentication import BBITokenAuthentication

from datetime import datetime, timedelta
from pytz import utc


class BearerAuthentication(BBITokenAuthentication):
    keyword = 'Bearer'
