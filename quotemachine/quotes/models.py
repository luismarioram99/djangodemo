from django.db import models
from django.conf import settings
# Create your models here.
class Quote(models.Model):
    id      = models.IntegerField(primary_key=True, auto_created=True)
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=140, null=False, blank=False)

    def __str__(self):
        return "quote #" + str(self.id) + " by " + str(self.author)