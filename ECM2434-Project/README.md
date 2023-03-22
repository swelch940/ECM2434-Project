# ECM2434-Project
ECM2434 Group Software Engineering Project
Group 23
# BARK BUDDIES

## Introduction

This game is a scrum project application that uses a django interface to run the bark buddy game where you have to log in to play, the logged in users are stored both on the django **admin page** and on the **sql login database**. Each player gets a tree pet which if they complete sustainable activities, such as using the water fountains on campus, which we can check through geolocation, the player gets points and the bark pet gets bigger and the points are given in the oxygen saved, plastic saved on water bottles and water saved. There is a leaderboard for the tree score, so each player can see the other tree points.

For people that leave campus, they can keep their process without losing pointds by putting their bark buddy on a greenhouse where it would be stored without losing functionality.

### How to use the project

BARK BUDDIES is run through manage.py in the mysite folder, mysite contains all the django settings and the home folder contains all the html templates and python files

Templates contains the html files for the project and the functionality of the game

### For Developers

To set up the project on your machine:

- First, ensure you have Django installed on your machine. If you don't, you can install it using `pip install Django`.
- You will also need to ensure you have Crispy forms on your machine. If you don't, you can install it using `pip install crispy-bootstrap5`.
- Secondly, download an sql server to run your application on the backend, we recommend **xamp** for better functionality.
<https://www.apachefriends.org/download.html>
- Third, navigate to the directory you installed this repository to in the command line and run `python manage.py migrate`
- Lastly, to run the project use the command `python manage.py runserver`, open a browser and go to the localhost IP address `127.0.0.1:8000`.

The project is laid out like a standard Django project. We have one app - `home` - and the main site directory is `mysite`. All of our web templates can be found in the `templates` folder.

### Testing

The test are refered to the functionality of the game

- **tests.py**

### File Management

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

## Details

- Project Created by **Luis Hidalgo**, **Steven Welch**, **Joshua Curry**, **Callum Wilton** and **Nahum Hillier**
- Github repository: **<https://github.com/swelch940/ECM2434-Project>**
