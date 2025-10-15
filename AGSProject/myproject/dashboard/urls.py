from django.urls import path
from . import views

urlpatterns = [
    path('flavors/', views.flavors, name='flavors'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('packaging/', views.packaging, name='packaging'),
    path('toppings/', views.toppings, name='toppings'),
]
