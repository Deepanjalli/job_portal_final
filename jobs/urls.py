from django.contrib import admin
from django.urls import path, include
from jobsapp.views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = "jobs"

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('about', AboutView.as_view(), name='about'),
    path('', include('jobsapp.urls')),
    path('', include('accounts.urls')),
    path('api/', include([
        path('', include('jobsapp.api.urls')),
    ])),
]
