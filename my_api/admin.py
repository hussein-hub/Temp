from django.contrib import admin

# Register your models here.

# register all my models from the models.py file
from .models import *

admin.site.register(Property)
