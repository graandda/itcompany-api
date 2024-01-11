from rest_framework import generics
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer


class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
