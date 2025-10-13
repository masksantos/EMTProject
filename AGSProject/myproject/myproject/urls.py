# In myproject/myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView  # <-- ADD THIS IMPORT

urlpatterns = [
    # 1. ADD THIS LINE: Redirects the root path ('') to the login page
    path('', RedirectView.as_view(pattern_name='login', permanent=False), name='index'), 
    
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')), 
]