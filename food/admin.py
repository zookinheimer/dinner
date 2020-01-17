from django.contrib import admin
from .models import dinner_list, history

# Register your models here.
admin.site.register(dinner_list)
admin.site.register(history)