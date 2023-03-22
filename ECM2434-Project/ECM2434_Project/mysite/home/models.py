from django.db import models

class Accounts(models.Model):
    username = models.CharField(max_length=32,primary_key=True,unique=True)
    email = models.CharField(max_length=48,unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

class Tree(models.Model):
    username = models.CharField(max_length=32,primary_key=True,unique=True)
    oxygen = models.BigIntegerField(default=0)
    level = models.SmallIntegerField(default=1)
    plastic_saved = models.BigIntegerField(default=0)
    isAlive = models.BooleanField(default=True)
    endurance = models.SmallIntegerField(max_length=10)
    water = models.SmallIntegerField(default=20)
    bottle_plastic = models.IntegerField(default=500)
    
    def __str__(self):
        return self.username

    
    def get_leaderboard(self):
        return self.username, self.oxygen, self.plastic_saved