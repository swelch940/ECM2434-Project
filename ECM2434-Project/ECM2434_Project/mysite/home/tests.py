from django.test import TestCase
import asyncio



# Create your tests here.


#Testing the URLS are working
class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_mappage(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)
    
    def test_leaderboardpage(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
    
    #Failes due to unknown reason. May be due to needing to log in.
    def test_treepage(self):
        response = self.client.get('/tree')
        self.assertEqual(response.status_code, 200)
    
    def test_loginpage(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_registerpage(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    
    
