01 basic info

1. Django is framework.
2. MVT (Model View Template) Similar to MVC.
3. Why Django - Fast, Feature Pack, Secure, Scalability.

02 create project
1. pip (Installer manager for python)
2. pip commands 
- pip install virtualenvwrapper-win
- mkvirtualenv test
- pip install django
- django-admin --version
- django-admin startproject project
- cd .\server\
- python manage.py runserver

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
1. Modal is for data. like database, schema
2. Template is the normal HTML, CSS, JS but it will also have DTL.
3. View process the request means logical part. also Modal to Template
1. GET method send data through query param. its visible in the url.  also increase url length
2. POST method is secure and prevent visible in url.

06 Model View Template | MVT
1. Modal is for data. like database, schema
2. Template is the normal HTML, CSS, JS but it will also have DTL.
3. View process the request means logical part. also Modal to Template
