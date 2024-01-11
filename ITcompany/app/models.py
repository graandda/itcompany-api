from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return f"{self.name} {self.surname}"
