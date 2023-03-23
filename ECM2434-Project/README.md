# ECM2434-Project
ECM2434 Group Software Engineering Project
Group 23
# BARK BUDDIES

## Table of Contents

### 1. [Introduction](#Introduction)
### 2. [Requirements](#requirements)
### 3. [How to run](#Howtorun)
### 4. [Testing](#Testing)
### 5. [Cloud Deployment](#CloudDeployment)
### 6. [File management](#Filemanagement)
### 7. [Details](#Details)

## Introduction <a name="Introduction"></a>

This game is a scrum project application that uses a django interface to run the bark buddy game where you have to log in to play, the logged in users are stored both on the django **admin page** and on the **sql login database**. Each player gets a tree pet which if they complete sustainable activities, such as using the water fountains on campus, which we can check through geolocation, the player gets points and the bark pet gets bigger and the points are given in the oxygen saved, plastic saved on water bottles and water saved. There is a leaderboard for the tree score, so each player can see the other tree points.

For people that leave campus, they can keep their process without losing points by putting their bark buddy on a greenhouse where it would be stored without losing functionality.

### Requirements <a name="requirements"></a>

Users can use the requirements.txt to install all the necessary dependecies for the application to run. 


```console
pip install -r requirements.txt
```
Users can also find all the libraries used listed in the requirements.txt file. 

User will also be required to obtain their own Google maps API key. Once obtained, users can insert their API key in map.html on line 193 and line 195.

### How to run <a name="Howtorun"></a>

BARK BUDDIES is run through manage.py in the mysite folder, mysite contains all the django settings and the home folder contains all the html templates and python files.

To run the server, users should first navigate to the outer mysite directory and run the folllowing commands in their terminal.


```console
python3 manage.py makemigrations
python3 manage.py migrate
```

Users can then start the server by pasting the following command in their terminal. 


```console
python3 manage.py runserver
```
This will start the django server locally and the user is able to freely play the game or see any changes they've made to the code.


### Testing <a name="Testing"></a>

The main tests of the application can be found in tests.py and users can run the tests by coping the following command in their terminal.


```console
python3 manange.py test
```
### Cloud Deployment <a name="CloudDeployment"></a>

This application is currently hosted on Railway's cloud deployment system. 

The url for the website is: https://ecm2434-project-production-582c.up.railway.app/

### File Management <a name="Filemanagement"></a>

- ECM2434-Project
  - mysite
    - home
      - _pycache_
      - BarkBuddy
        - barkpickler.py
      - migrations
        - _pycache_
        - _init_.py
      - static
        - images
          - background.jpeg
          - graphic-tree-hill_46176-136-_1_.jpg
          - transparent.jpeg
        - homestyle.css
        - loginstyle.css
        - map.css
        - newemail.css
        - newpassword.css
        - register.css
        - settings.css
        - treestats.css
      - _init_.py
      - admin.py
      - apps.py
      - bark_buddy.py
      - models.py
      - tests.py
      - urls.py
      - views.py
    - mysite
      - _pycache_
      - _init_.py
      - asgi.py
      - forms.py
      - settings.py
      - urls.py
      - wsgi.py
    - templates
    - register
      - register.html
    - registration
      - login.html
    - about.html
    - bottlesize.html
    - createaccount.html
    - deleteaccount-html
    - home.html
    - leaderboard.html
    - logo.png
    - map.html
    - newemail.html
    - newpassword.html
    - settings.html
    - tree.html
    - db.sqlite3
    - manage.py
    - requirements.txt
  - license
  - PRIVACY-POLICY.txt
  - Procfile
  - README.md
  - runtime.txt

## Details <a name="Details"></a>

- Project Created by **Luis Hidalgo**, **Steven Welch**, **Joshua Curry**, **Callum Wilton** and **Nahum Hillier**
- Github repository: **<https://github.com/swelch940/ECM2434-Project>**
