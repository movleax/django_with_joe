from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    firstName = models.CharField(max_length=225)
    lastName = models.CharField(max_length=225)
    createdat = models.DateTimeField(auto_now_add=True)
    updateddat = models.DateTimeField(auto_now=True)

class Games(models.Model):
    name = models.CharField(max_length=225)
    createdat = models.DateTimeField(auto_now_add=True)
    updateddat = models.DateTimeField(auto_now=True)

class Scores(models.Model):
    games_id = models.ForeignKey(Games, on_delete=models.CASCADE, related_name = 'gamescores')
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='userscores')
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

class ScoresViewModel():
    gameName: str
    userName: str
    score: int
    timestamp: DateTime