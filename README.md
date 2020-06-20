# Django Portfolio

Home page
![alt text](https://github.com/weslleylc/django-portfolio/blob/master/portfolio/static/portfolio/img/django_project.png)

Usage
-----
Portfolio Project Build with Django 3

Getting Started
Basic instructions to running on your local machine.

Prerequisites:

    python== 3.8 or up and django==3.0.7, pillow==7.1.2

Installing

Clone the repo:

    git clone https://github.com/weslleylc/django-portfolio.git
    cd django-portfolio

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

 
To migrate the database open terminal in project directory and type:

    python manage.py makemigrations
    python manage.py migrate

To use admin panel you need to create super user using this command:

    python manage.py createsuperuser

To run the program in local server use the following command:

    python manage.py runserver
    
Go to admin painel and create a Profile, them associete this profile with your user:
    
    http://127.0.0.1:8000/admin/

Open the web application:
  
    http://127.0.0.1:8000/

# To Do
    Blog application 

