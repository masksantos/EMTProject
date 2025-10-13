from django.urls import path
from . import views

# NOTE: The names 'login' and 'logout' used here must match the names 
# referenced in your redirect calls in views.py.
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Add any other account-related paths (like signup, password reset) here
]
