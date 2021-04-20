from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from datetime import date
from places.models import Place
from django.utils import timezone


class Event(TimeStampedModel):
    title = models.CharField(max_length=250)
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    event_time = models.DateTimeField(default=timezone.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{0}'.format(self.title, self.host)

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

class EventTime(models.Model):
    event = models.ForeignKey('Event',on_delete=models.SET_NULL,null=True)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    def __str__(self):
        return str(self.date)
