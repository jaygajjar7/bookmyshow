
# BookMyShow

## :rocket: Demo Application
:point_right: (https://bookmyshowaberdeen.herokuapp.com/) <br>


## About
BookMyShow is India's biggest online movie and events ticketing brand. The website caters to ticket sales for movies, plays, concerts and sporting events via the online platform. Launched in 2007, it is headquartered in Mumbai, Maharashtra. It additionally has offices in New Delhi, Bangalore, Hyderabad, Chennai and Kolkata.

## Installation

We can start developing our application to display the data. Create a new project folder called 'Bookmyshow' and then cd into the folder via the terminal and execute these commands:

```bash
pyenv local 3.9.0 
python3 -m venv .venv
source .venv/bin/activate 
pip install --upgrade pip [ this is optional]
```

So after getting this done we have to install basic libraries

```bash
pip install Django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 
```

### Testing Credentials
User Side <br>
Url: https://bookmyshowaberdeen.herokuapp.com/login/ <br>
Username: daarionaharis <br>
Password: Jayg@1997 <br>

Admin Side <br>
Url: https://bookmyshowaberdeen.herokuapp.com/admin <br>
username: admin <br>
password: Jayg@1997 <br>

## Installed Packages

| Name | Version |  
| ----------- | ----------- |
|dj-database-url|0.5.0|
|gunicorn|20.1.0
|Django|3.0.7|
|django-allauth|0.41.0|
|django-crispy-forms|1.9.0|
|django-debug-toolbar|2.2|
|Pillow|7.0.0|
|python-decouple|3.3|
|sorl-thumbnail|12.6.3|
|python-decouple|3.3|
|django-widget-tweaks|1.4.8|
|django-recaptcha|3.0|
|six|1.14.0|
