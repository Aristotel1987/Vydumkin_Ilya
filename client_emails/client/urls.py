from django.urls import path
from .views import client_list, register_client, delete_client

urlpatterns = [
       path('', client_list, name='client_list'),
       path('register/', register_client, name='register_client'),
       path('delete/<int:client_id>/', delete_client, name='delete_client'),
   ]