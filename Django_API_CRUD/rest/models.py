import json
from django.conf import settings
from django.db import models
from django.core.serializers import serialize

# Create your models here.

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('user', 'content', 'image', 'pk'))
        return json.dumps(list_values)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

def upload_rest_image(instance, filename):
    return "rest/{user}/{filename}".format(user=instance.user, filename=filename)

class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_rest_image, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()
    def __str__(self):
        return str(self.content)[:30]

    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            "content":self.content,
            "user":self.user.pk,
            "image":image,
        }
        data = json.dumps(data)
        return data