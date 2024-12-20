from datetime import timedelta
from django.conf import settings
"""
Provides access to settings.
Returns defaults if not set.
"""

class CustomSettings(object):

    """Provides settings as defaults for working with tokens."""

    @property
    def TOKEN_DURATION(self):
        """
        Return the allowed lifespan of a token as a TimeDelta object.
        Defaults to 30 minutes
        """
        try:
            val = settings.TOKEN_DURATION
        except AttributeError:
            # val = timedelta(minutes=30)
            val = timedelta(minutes=480)

        return val


custom_settings = CustomSettings()
