00 useful commands

- `python .\manage.py runserver`
- `python .\manage.py startapp travel`
- `python .\manage.py collectstatics`

01 basic info Django

1. Django is Free and open-source framework for building web apps with python.
2. we have simillir frameworks (Flask, Tornado)
3. Companies using (YouTube, Instagram, Spotify, Dropbox)
4. Django is batteries included framework it comes with lots of feature out of box so we dont have make it from strach. 
 -The admin side interface
 - Object-relational mappper (ORM)
 - Authentication
 - Caching
6. Django work on MVT (Model View Template) Similar to MVC.
7. Why Django - Fast, Feature Pack, Secure, Scalability.

02 create project

1. pip (Installer manager for python)
2. pip commands

- `pip install virtualenvwrapper-win`
- `mkvirtualenv test`
- `pip install django`
- `django-admin --version`
- `django-admin startproject project`
- `cd .\server\`
- `python manage.py runserver`

03 First App

1. python manage.py startapp calc
2. create urls.py inside calc and make one route
3. make function is views.py and return HttpResponse Hello World
4. include urls.py in main urls.py
5. python manage.py runserver

04 Django Template Language | DTL

1. create folder ex. templates and home.html file.
2. change in settings.py
   'DIRS': [os.path.join(BASE_DIR, 'template')],
3. also change in views.py
4. render(req, 'home.html')
5. you can also send data from views in dictionary like
render(req, 'home.html', {'name': 'Adnan'})
<h1>Hello {{name}}!!!</h1>

05 GET vs POST HTTP method

1. GET method send data through query param. its visible in the URL. also increase URL length
2. POST method is secure and prevent visible in URL.

06 Model View Template | MVT

1. Modal is for data. like database, schema
2. Template is the normal HTML, CSS, JS but it will also have DTL.
3. View process the request means logical part. also Modal to Template

07 Static Files

1. Static Files are user cannot interaction with UI.
2. like html CSS
3. we can serve Static Files from Django

```
STATIC_URL = '/static/'
STATICFILES = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
```

4. in django we used this command to use static files
   `python .\manage.py collectstatics`
5. you have href when you send css and other file
   `{% load static %}`
   `{% static 'file_path' %}`
