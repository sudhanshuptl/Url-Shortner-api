# Url-Shortner-api
This tool can be used to generate short url and also can be used to upload a file and get a short url to fetch that file

# Setup Virtual Environment
 1. Install package `pip install virtualenv`
 2. Create virtual environment `virtualenv yourenv -p python3.7`
 3. Activate virtual environment (mac/linux) `source mypython/bin/activate` 
 4. Activate virtual environment(Windows) `mypthon\Scripts\activate`
 5. Install Django : `pip install django`
 6. Install Django rest Framework `pip install djangorestframework`
 7. Deactivate virtualenv `deactivate`
 
# Django Basic Commands <[Read Full Doc](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)>
* Create Project `django-admin startproject myproject`
* Move to project Dir and Run server `python manage.py runserver`
* Create an app `python manage.py startapp app_name`
* Migrate database `python manage.py makemigrations app_name`
* See the changes made in migration `python manage.py sqlmigrate app_name migration_id(ex 0001)`
