from django.shortcuts import render
from django.views import generic
from .models import Event

def index(request):
    return render(request, 'index.html',)

class EventListView(generic.ListView):
    model = Event
    paginate_by = 2

