**00 useful commands**

- To Run server `python .\manage.py runserver`
- To create app `python .\manage.py startapp playground`
- To collect static file `python .\manage.py collectstatic`

**01 basic info**

1. Django is Free and open-source framework for building web apps with python.
2. we have simillir frameworks (Flask, Tornado)
3. Companies using (YouTube, Instagram, Spotify, Dropbox)
4. Django is batteries included framework it comes with lots of feature out of box so we don't have make it from scratch.
 - The admin side interface
 - Object-relational mapper (ORM)
 - Authentication
 - Caching
6. Django work on MVT (Model View Template) Similar to MVC.
7. Why Django - Fast, Feature Pack, Secure, Scalability.

**02 create project**

1. pip (Installer manager for python)
2. pip command
3. Pipfile is like package.json

- `pip install pipenv`
- `pipenv install django`
- `pipenv shell`
- `django-admin --version`
- `django-admin startproject storefront` (delete folder and type `django-admin startproject storefront .` to avoid addition directory)
- `python .\manage.py startapp account`
- `pip install virtualenvwrapper-win` (optional)
- `mkvirtualenv test` (optional)
- `python manage.py runserver`

**03 Folder Structure**
- when we create django app. so every django app has exact same structure.
1. admin module - here we define how the admin interface for this app is going to look like.
2. app module - here we configure this app.
3. models module - where we define the modal classes for this app we use modal classes to pull out data from database.
4. tests module - for write out unit tests.
5. views module - for request handler or controller
6. settings module - every time when create a it must add in settings module.
7. urls module - where we define the our routes.
8. templates folder - template for return html content to the client here we can write html.

**04 First App**

1. python manage.py startapp calc
2. create urls.py inside calc and make one route
3. make function is views.py and return HttpResponse Hello World
4. include urls.py in main urls.py
5. python manage.py runserver

**05 Django Template Language | DTL**

1. create folder ex. templates and home.html file.
2. change in settings.py
   'DIRS': [os.path.join(BASE_DIR, 'template')],
3. also change in views.py
4. render(req, 'home.html')
5. you can also send data from views in dictionary like
render(req, 'home.html', {'name': 'Adnan'})
<h1>Hello {{name}}!!!</h1>

**06 GET vs POST HTTP method**

1. GET method send data through query param. its visible in the URL. also increase URL length
2. POST method is secure and prevent visible in URL.

**07 Model View Template | MVT**

1. Modal is for data. like database, schema
2. Template is the normal HTML, CSS, JS but it will also have DTL.
3. View process the request means logical part. also Modal to Template

**08 Static Files**

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
5. you have modify href when you send css and other file
   `{% load static %}`
   `{% static 'file_path' %}`


**09 Insatlling Django Debug Toolbar**
1.  pip install django-debug-toolbar
 ```
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware",]
INTERNAL_IPS = ["127.0.0.1",]
INSTALLED_APPS = ['debug_toolbar',]
path("__debug__/", include("debug_toolbar.urls")),
```

**10 Models and Migrations in Django**

**11 Making route using fastapi pakate**
`virtualenv env`
`cd .\env\Scripts\`
`./Activate`
`https://github.com/astral-sh/uv`
`pip install uv`
`uv pip install fastapi uvicorn`
`python .\app.py `

