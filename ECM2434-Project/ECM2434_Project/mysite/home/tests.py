#@authors Steven Welch

from django.test import TestCase
import asyncio
from . import bark_buddy


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


#Currently under construction. 
class BarkBuddyTest(TestCase):
    
    
    testbuddy = bark_buddy.TestBuddy(12345, "test")
    
    #Test to see if the murder tree fucntions works.
    def test_assert_murder(self):
        self.testbuddy.murder_tree()
        try:
            assert self.testbuddy.alive == False
        except(AssertionError):
            return False
        else: return True
    
    #Test to see if the water function of the tree is working.
    def test_assert_water_tree(self):
         try:
             assert self.testbuddy.water + 5 == self.testbuddy.water_tree()
         except(AssertionError):
            return False
         else: return True
    
    #Asserts that the tree can level up
    def test_level_up(self):
        try:
            assert self.testbuddy.level_handling() == self.testbuddy.level + 1
        except(AssertionError):
            return False
        else: return True


#More extensive testing needed for the bark_buddy class as we integrate.
    
    
