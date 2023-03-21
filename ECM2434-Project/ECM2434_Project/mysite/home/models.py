from django.db import models
from django.contrib.auth.models import User
from django.db import connection
class Leaderboard(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.player.username
    



def getLeaderboard():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT auth_user.username, leaderboard.oxygen-saved
            FROM auth_user
            INNER JOIN leaderboard ON auth_user.id = leaderboard.user_id
            ORDER BY leaderboard.oxygen-saved DESC
            LIMIT 10
        ''')
        rows = cursor.fetchall()
    return rows






