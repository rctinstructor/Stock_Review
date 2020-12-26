from django.contrib import admin
from .models import *

# Register your models here.
class MyStock(admin.ModelAdmin):
    list_display = ('name', 'description', 'Evaluation', 'year', 'star', 'show')
    list_filter = ('star', 'show')

admin.site.register(Stock, MyStock)