from django.db import models

from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from places.models import Place


class Event(TimeStampedModel):
    title = models.CharField(max_length=250)
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.title, self.host)

