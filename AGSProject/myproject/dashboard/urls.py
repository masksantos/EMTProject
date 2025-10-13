from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('notifications/', views.notifications, name='notifications'),
    path('log-history/', views.log_history, name='log_history'),
    path('about/', views.about, name='about'),

    path('flavors/', views.flavors, name='flavors'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('toppings/', views.toppings, name='toppings'),
    path('packaging/', views.packaging, name='packaging'),
]
=======
    path('', views.home, name='home'),  # default route for dashboard home
    path('inventory/', views.inventory, name='inventory'),
    path('notifications/', views.notifications, name='notifications'),
    path('log_history/', views.log_history, name='log_history'),
    path('about/', views.about, name='about'),
]

>>>>>>> 3f2e4059f08fe8e95e55caf3cf6cbf639dacf92b
