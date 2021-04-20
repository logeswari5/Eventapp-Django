from django.contrib import admin

from .models import Event, EventTime

admin.site.register(Event)
admin.site.register(EventTime)