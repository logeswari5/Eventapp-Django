from . import views
from django.urls import path


urlpatterns = [

    path('', views.index, name="index"),
    path('listofevents/',views.EventListView.as_view(),name="list-of-events"),
    path('event/<int:pk>/',views.EventDetailView.as_view(),name="event-detail"),
    path('event/new/',views.event_new,name='new-event'),
    path('all_hosts/', views.all_hosts, name='all-hosts'),
    path('event/host/<str:inputhost>/',views.host_events, name="host-events"),
    path('delete_event/<int:pk>/',views.deleteEvent, name="delete-vent"),
    path('event/timings/<int:pk>/',views.eventtime_new, name="new-event"),
    path('update_event/<int:pk>/', views.updateEvent, name="update_event"),
]