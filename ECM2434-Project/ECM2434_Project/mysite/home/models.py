from django.db import models
from django.utils import timezone


class Tree(models.Model):#tree table
    username = models.CharField(max_length=32,primary_key=True,unique=True)#owner's name
    oxygen = models.BigIntegerField(default=0)#oxygen produced over tree's lifetime
    level = models.SmallIntegerField(default=1)#level of the tree, determines growth
    plastic_saved = models.BigIntegerField(default=0)#amount of plastic saved, in grams
    isAlive = models.BooleanField(default=True)#whether tree is suffering
    water = models.SmallIntegerField(default=20)#current water %
    in_greenhouse = models.BooleanField(default=False)#whether tree is in the ghouse :fire:
    last_active = models.DateTimeField(default=timezone.now())#last time tree was accessed
    bottle_plastic = models.IntegerField(default=500)#size of plastic bottle
    
    def __str__(self):
        return self.username

    
    def get_leaderboard(self):
        return self.username, self.oxygen, self.plastic_saved