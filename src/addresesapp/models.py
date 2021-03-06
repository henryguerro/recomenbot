from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    mail = models.EmailField(max_length=255, blank=True, null=True)

    # display name on admin panel
    def __str__(self):
        return self.name


