from django.test import TestCase
from django.test import Client
from django.urls import reverse
import asyncio
from django.test import RequestFactory
from .views import *
from django.contrib.auth.models import AnonymousUser, User

from .models import Tree


# Create your tests here.


#Testing to make sure the connection with the urls are all working.
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

    def test_treepage(self):
        response = self.client.get('/tree')
        self.assertEqual(response.status_code, 200)
    
    def test_loginpage(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_registerpage(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_settingspage(self):
        response =self.client.get('/settings/')
        self.assertEqual(response.status_code, 200)
    
    def test_aboutpage(self):
        response =self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_registerpage(self):
        response =self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_deleteaccountpage(self):
        response =self.client.get('/deleteaccount/')
        self.assertEqual(response.status_code, 200)
    
    def test_newemail(self):
        response =self.client.get('/newemail/')
        self.assertEqual(response.status_code, 200)
    
    def test_newpassword(self):
        response =self.client.get('/newpassword/')
        self.assertEqual(response.status_code, 200)
    
    def test_bottlesize(self):
        response =self.client.get('/bottlesize/')
        self.assertEqual(response.status_code, 200)





#Testing to see if we can create Tree model and change model values. 
class TestModel(TestCase):

    #setting up tree object.
    def setUp(self):
        self.tree1 = Tree.objects.create(username = 'test1')
    
    #testing to see if the tree has been created
    def test_tree_is_created(self):
        self.assertEquals(self.tree1.username, "test1")
    
    #testing to see if we can change the water value.
    def test_changing_water_value(self):
        water = self.tree1.water
        self.tree1.water += 10

        try:
            self.assertFalse(water, self.tree1.water)
        except(AssertionError):
            return False
        else:
            return True
    
    #testing to see if we can change the oxygen value.
    def test_changing_oxygen_value(self):
        oxygen = self.tree1.oxygen
        self.tree1.oxygen += 20

        try:
            self.assertFalse(oxygen, self.tree1.oxygen)
        except(AssertionError):
            return False
        else:
            return True
    
    #testing to see if we can change a username.
    def test_changing_username(self):
        username = self.tree1.username
        self.tree1.username = "change"

        try:
            self.assertFalse(username, self.tree1.username)
        except(AssertionError):
            return False
        else:
            return True
    
    #testing to see if we can change levels
    def test_changing_level(self):
        level = self.tree1.level
        self.tree1.level += 1

        try:
            self.assertFalse(level, self.tree1.level)
        except(AssertionError):
            return False
        else:
            return True
    
    #testing to see if we can kill a tree.
    def test_changing_isAlive(self):
        isAlive = self.tree1.isAlive
        self.tree1.isAlive = False

        try:
            self.assertFalse(isAlive, self.tree1.isAlive)
        except(AssertionError):
            return False
        else:
            return True
    
    #testing to see if we can change greenhouse value.
    def test_changing_in_greenhouse(self):
        in_greenhouse = self.tree1.in_greenhouse
        self.tree1.isAlive = True

        try:
            self.assertFalse(in_greenhouse, self.tree1.in_greenhouse)
        except(AssertionError):
            return False
        else:
            return True
    
    #testing to see if we can change plastic value.
    def test_changing_plastic_saved(self):
        plastic_saved = self.tree1.plastic_saved
        self.tree1.plastic_saved += 10

        try:
            self.assertFalse(plastic_saved, self.tree1.plastic_saved)
        except(AssertionError):
            return False
        else:
            return True
    
    
        
class TestViews(TestCase):
    def setUp(self):

        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@…', password='test123')

    #Testing to see if a user can delete their account.
    def test_delete_account(self):
        self.test1 = User.objects.create_user(
            username='test1', email='test@…', password='test123')
        request = self.factory.get('/deleteaccount/"Deleted=yes"')
        
        
        request.user = self.test1
        response = deleteaccount(request)
        self.assertEqual(response.status_code, 200)
        


    #Testing to see if a user can chnage email.
    def test_newewmail(self):
        request = self.factory.get('/newemail')

        request.user = self.user
        response = newemail(request)
        self.assertEqual(response.status_code, 200)
    
    #Testing to see if register user works.
    def test_register(self):
        request = self.factory.get('/register')

        request.user = self.user
        response = register(request)
        self.assertEqual(response.status_code, 200)
    
    



        

      
    
    
    


    
    
