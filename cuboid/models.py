from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Cuboid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE) 
    length = models.IntegerField(null=True, blank=True)
    breadth = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    area = models.IntegerField(null=True, blank=True, default=0)
    volume = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.user.username)

    def get_api_url(self, request=None):
        return api_reverse("cuboid-rud", kwargs={'pk': self.pk}, request=request)

    def save(self, *args, **kwargs):
        if getattr(self, '_length_changed', True):
            self.area = self.length*self.breadth
            self.volume = self.length*self.breadth*self.height
        if getattr(self, '_breadth_changed', True):
            self.area = self.length*self.breadth
            self.volume = self.length*self.breadth*self.height
        if getattr(self, '_height_changed', True):
            self.volume = self.length*self.breadth*self.height
        super(Cuboid, self).save(*args, **kwargs)
    