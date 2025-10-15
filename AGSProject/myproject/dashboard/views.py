from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def flavors(request):
    return render(request, 'dashboard/flavors.html')

@login_required
def ingredients(request):
    return render(request, 'dashboard/ingredients.html')

@login_required
def packaging(request):
    return render(request, 'dashboard/packaging.html')

@login_required
def toppings(request):
    return render(request, 'dashboard/toppings.html')
