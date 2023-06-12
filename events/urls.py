"""event_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin

from django.urls import path
from .views import (
    EventListCreateView,
    EventUpdateView,
    TicketCreateView,
    TicketDetailView,
)

from . import views

urlpatterns = [
path('',views.getData),
    path('events/', EventListCreateView.as_view(), name='event-list-create'),

    path('events/<int:pk>/', EventUpdateView.as_view(), name='event-update'),
    path('tickets/', TicketCreateView.as_view(), name='ticket-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]

