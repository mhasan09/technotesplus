from django.db import models
from django.contrib.auth.models import User


class NOTE(models.Model):
    CREATED_BY = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    TITLE = models.TextField("TITLE",max_length=512, null=False, blank=False)
    CONTENT = models.TextField("CONTENT", null=False, blank=False)
    CREATED_AT = models.DateTimeField("TIME_STAMP", null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.TITLE


