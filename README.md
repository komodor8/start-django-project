# start-django-project

fresh django app to test features with bootstrap 4, models (Author, Book), extends, views, urls, settings


## Steps
1. Create and activate your Virtualenv
```
virtualenv -p python3 `envname`
$ source /path/to/ENV/bin/activate
```

2. Create your project
```
django-admin startproject `mysite`
```

3. Install the depedencies
```
pip install Django
pip install django-debug-toolbar
pip install psycopg2-binary
python manage.py migrate
```


## What's inside:
+ django version 3.0
+ debug toolbar
+ app 'testingapp' with 2 models:
  + Author, Books (in admin also)
+ Bootstrap 4
+ extends templates base.html

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
