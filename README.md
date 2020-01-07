# start-django-project

Fresh django project for fast testing with bootstrap 4, models (Author, Book), extends, views, urls, settings


## Steps
1. Create and activate your virtualenv
```
virtualenv -p python3 ***envname***
source /path/to/ENV/bin/activate
```

2. Create your project
```
django-admin startproject ***mysite***
```

3. Install the depedencies to the activated environment and migrate
```
pip install Django
pip install django-debug-toolbar
pip install psycopg2-binary
python manage.py migrate
```

4. Create super user for the admin dashboard
```
python manage.py createsuperuser
```

## What's inside:
+ django version 3.0
+ debug toolbar
+ app 'testingapp' with 2 models:
  + Author, Books (in admin also)
+ Bootstrap 4
+ extends templates base.html

```
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOUR_DB_NAME',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'XX.XX.XXX.83',
        'PORT': '5432',
    }
}
```
