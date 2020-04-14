from django.contrib import admin
from django.urls import path, include
import myapp.views
import myapp.urls
import myapp2.views
import myapp2.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('myapp2.urls')),
    path('', myapp.views.home, name="home"),
    path('info/', myapp2.views.info, name="info"),  
    path('people/', myapp2.views.people, name="people"),
    
]
