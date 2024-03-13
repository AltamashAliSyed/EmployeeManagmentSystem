from django.contrib import admin
from mng_app.models import Department,Role,Employee,Feedback
# Register your models here.

admin.site.register((Department,Role,Employee,Feedback))
#Username (leave blank to use 'shree'): EMP123
#Email address:
#Password:
#Password (again):
#This password is too short. It must contain at least 8 characters.
#Superuser created successfully