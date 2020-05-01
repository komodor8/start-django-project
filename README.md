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

3. Set database & [ Allow remote connections to PostgreSQL](http://devopspy.com/linux/allow-remote-connections-postgresql/)
```
Step 1 – Update postgres.conf
Step 2. Configuring pg_hba.conf
`$ sudo vi /etc/postgresql/9.6/main/pg_hba.conf`
Step 3. Restart PostgreSQL Server
`$ sudo systemctl restart postgresql`
Step 4. Adjusting Firewall (optional)
`$ sudo ufw allow 5432/tcp`
```

4. Install the depedencies to the activated environment and migrate
```
pip install Django
pip install django-debug-toolbar
pip install psycopg2-binary
python manage.py migrate
```

5. Create super user for the admin dashboard
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
        'PASSWORD': 'secret',
        'HOST': 'XX.XX.XXX.42',
        'PORT': '5432',
    }
}
```
