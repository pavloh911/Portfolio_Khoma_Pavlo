from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_url'),
    path('message', views.messege, name='message'),
    path('messages_for_us', views.view_massages, name='messages_for_us'),
    path('change_status', views.change_status, name='change_status'),
]