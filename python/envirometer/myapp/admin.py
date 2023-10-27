from django.contrib import admin

# Register your models here.
from .models import MyModel  # Import your model

admin.site.register(MyModel)