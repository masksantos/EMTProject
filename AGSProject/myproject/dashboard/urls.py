from django.urls import path
from . import views

urlpatterns = [
    # Main dashboard page
    path('', views.home, name='home'),
    
    # Inventory link (Fixing the NoReverseMatch error)
    path('inventory/', views.inventory, name='inventory'), 
    
    # Other dashboard pages
    path('flavors/', views.flavors, name='flavors'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('toppings/', views.toppings, name='toppings'),
    path('packaging/', views.packaging, name='packaging'),
    path('notifications/', views.notifications, name='notifications'),
    path('log-history/', views.log_history, name='log_history'),
    path('about/', views.about, name='about'),
]
