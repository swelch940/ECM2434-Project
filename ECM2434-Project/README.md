=======
# ECM2434-Project
ECM2434 Group Software Engineering Project
=======
# Tree Game

## Introduction

This game is a scrum project application that uses a django interface to run a tree game where you have to log in to play and each player gets a tree pet which if they complete sustainable activities, such as using the water fountains on campus, which we can check through geolocation, the player gets points and the pet gets bigger and the points are given in oxygen and water that you tree gets. There is a leaderboard for the tree score, so each player can see the other tree points.

### How to use the project

Tree game is run through manage.py in the mysite folder, mysite contains all the django settings and the home folder contains all the html templates and python files

Templates contains the html files for the project and the functionality of the game

### Testing

The test are refered to the functionality of the game

- **tests.py** 

### Running

To run the game run inside of the mysite folder **python manage.py runserver**, open a browser and go to **<http://127.0.0.1:8000/>**.

### File Management

- ECM2434-Project
  - mysite
    - home
      - _pycache_
      - BarkBuddy
        - barkbuddy_test.py
        - bark_buddy.py
        - barkpickler.py
      - migrations
        - _pycache_
        - _init_.py
      - static
        - images
          - background.jpeg
          - transparent.jpeg
        - homestyle.css
        - loginstyle.css
        - treestats.css
      - _init_.py
      - admin.py
      - apps.py
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
      - accountcreated.html
      - createaccount.html
      - home.html
      - leaderboard.html
      - login.html
      - logo.png
      - map.html
      - tree.html
    - db.sqlite3
    - manage.py
  - license
  - README.md

## Details

- Project Created by **Luis Hidalgo**, **Steven Welch**, **Joshua Curry**, **Callum Wilton** and **Nahum hillier**
- Github repostery: **<https://github.com/swelch940/ECM2434-Project>**
