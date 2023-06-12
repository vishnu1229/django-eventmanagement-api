from django.shortcuts import render


from rest_framework import generics
from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])

def getData(request):
    person = {'name':'vishnu','age':23}
    return Response(person)

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUpdateView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

