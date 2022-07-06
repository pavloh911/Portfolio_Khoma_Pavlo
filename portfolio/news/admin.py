from django.contrib import admin
from .models import News, Group_of_news

# Register your models here.

admin.site.register(News)
admin.site.register(Group_of_news)