from django.contrib import admin
from django.urls import path, include
from dashboard.views import login_view, logout_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),  # Home page/dashboard
    path('dashboard/', include('dashboard.urls')),  # if you have other dashboard routes
]
