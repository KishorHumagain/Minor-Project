from django.contrib import admin
from .models import dbms

@admin.register(dbms)
# Register your models here.
class dbmsAdmin(admin.ModelAdmin):
    list_display=('id','questions','marks')