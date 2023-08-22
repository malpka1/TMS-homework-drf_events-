"""
URL configuration for events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from events1.views import UserCreate, UserList, EventList, EventSubscribe, EventMyList, CreateEventView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserCreate.as_view(), name='user_create'),
    path('api/users/all/', UserList.as_view(), name='user_list'),
    path('api/events/', EventList.as_view(), name='event_list'),
    path('api/event/<int:pk>/', EventSubscribe.as_view(), name='event_subscribe'),
    path('api/events/my/', EventMyList.as_view(), name='event_my_list'),
    path('events/create/', CreateEventView.as_view(), name="event-create"),
]



