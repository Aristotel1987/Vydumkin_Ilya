from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('clients/', include('client.urls')),  # Это основной маршрут приложения
    path('', include('client.urls')),  ]