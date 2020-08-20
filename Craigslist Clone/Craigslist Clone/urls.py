from django.contrib import admin
from my_app import views
from django.urls import path, include

urlpatterns = [
    path('', include('my_app.urls')),
    path('admin/', admin.site.urls),

]
