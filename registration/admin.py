from django.contrib import admin
from .models import Organisation, Customer, Profile
from django.contrib.auth.models import User

admin.site.register(Customer)
admin.site.register(Organisation)
admin.site.register(Profile)

# Register your models here.
