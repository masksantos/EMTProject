from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # default route for dashboard home
    path('inventory/', views.inventory, name='inventory'),
    path('notifications/', views.notifications, name='notifications'),
    path('log_history/', views.log_history, name='log_history'),
    path('about/', views.about, name='about'),
]

