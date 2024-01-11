from django.urls import path
from .views import (
    TeamListCreateView,
    TeamDetailView,
    PersonListCreateView,
    PersonDetailView,
)

urlpatterns = [
    path("teams/", TeamListCreateView.as_view(), name="team-list-create"),
    path("teams/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("people/", PersonListCreateView.as_view(), name="person-list-create"),
    path("people/<int:pk>/", PersonDetailView.as_view(), name="person-detail"),
]
