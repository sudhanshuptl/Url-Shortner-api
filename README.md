# Url-Shortner-api
This tool can be used to generate short url and also can be used to upload a file and get a short url to fetch that file

# Setup Virtual Environment
 1. Install package `pip install virtualenv`
 2. Create virtual environment `virtualenv yourenv -p python3.7`
 3. Activate virtual environment (mac/linux) `source mypython/bin/activate` 
 4. Activate virtual environment(Windows) `mypthon\Scripts\activate`
 5. Install Django : `pip install django`
 6. Install Django rest Framework `pip install djangorestframework` `pip install djangorestframework-jwt`
 7. Deactivate virtualenv `deactivate`
 
# Django Basic Commands <[Read Full Doc](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)>
* Create Project `django-admin startproject myproject`
* Move to project Dir and Run server `python manage.py runserver`
* Create an app `python manage.py startapp app_name`
* Migrate database `python manage.py makemigrations app_name` It just create queries but does't execute it, next step make it happen in database.
* Migrate all `python manage.py migrate`
* See the changes made in migration `python manage.py sqlmigrate app_name migration_id(ex 0001)`
* Create admin user `python manage.py createsuperuser`


# Url Shortner
* SuperUser credentials `username: admin` `pass: root`
* Regirect to your url using `http://localhost:8000/myurl/<Your_site_code_you>` `Your_site_code_you` is unique code you got  when you registered your link
* you can also register at `http://localhost:8000/tinyurl/api/myurl/`

## rest_api
* Use url `http://localhost:8000/tinyurl/api/myurl/` for all rest api action



# Resources to refer
* [jwt](https://www.youtube.com/watch?v=Fhcn2qx-4VQ)