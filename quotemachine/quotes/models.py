from django.db import models
from django.conf import settings
# Create your models here.
class Quote(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=50, null=False, blank=False)
