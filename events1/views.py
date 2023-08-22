from rest_framework import generics
from django.contrib.auth.models import User
from .models import Event
from .serializers import UserSerializer
from django.utils import timezone
from .serializers import EventSerializer
from rest_framework import permissions


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventList(generics.ListAPIView):
    queryset = Event.objects.filter(meeting_time__gt=timezone.now())
    serializer_class = EventSerializer


class EventSubscribe(generics.UpdateAPIView):
    queryset = Event.objects.filter(meeting_time__gt=timezone.now())
    serializer_class = EventSerializer


class EventMyList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = User.objects.get(id=1)
        return Event.objects.filter(users=user)


class CreateEventView(generics.CreateAPIView):
    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



