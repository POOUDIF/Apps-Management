import binascii
import os

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from .settings import custom_settings


class BBIToken(models.Model):
    class Meta:
        app_label   = 'bbi_token'
        db_table    = 'bbi_token'
        verbose_name    = _("BBI Token")
        verbose_name_plural = _("BBI Tokens")

    key = models.CharField(_("Key"), max_length=50, primary_key=True)
    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL, related_name='auth_token',
    #     on_delete=models.CASCADE, verbose_name=_("User")
    # )
    username = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    expires = models.DateTimeField(_("Expires in"), )    
    
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()

        self.expires = timezone.now() + custom_settings.TOKEN_DURATION
        return super(BBIToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(25)).decode()

    def __str__(self):
        return self.key
