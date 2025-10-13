from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

# Ensure all views referenced in dashboard/urls.py are here

@login_required
def home(request: HttpRequest) -> HttpResponse:
    """Main dashboard page."""
    # Note: You may need to pass context data here later if home.html requires it.
    return render(request, 'dashboard/home.html')

@login_required
def flavors(request: HttpRequest) -> HttpResponse:
    """Flavors management page."""
    # Assuming 'flavors.html' needs its own data context here
    return render(request, 'dashboard/flavors.html')

@login_required
def ingredients(request: HttpRequest) -> HttpResponse:
    """Ingredients management page."""
    return render(request, 'dashboard/ingredients.html')

@login_required
def toppings(request: HttpRequest) -> HttpResponse:
    """Toppings management page."""
    return render(request, 'dashboard/toppings.html')

@login_required
def packaging(request: HttpRequest) -> HttpResponse:
    """Packaging management page."""
    return render(request, 'dashboard/packaging.html')

@login_required
def notifications(request: HttpRequest) -> HttpResponse:
    """Notifications page."""
    return render(request, 'dashboard/notifications.html')

@login_required
def log_history(request: HttpRequest) -> HttpResponse:
    """Log history page."""
    return render(request, 'dashboard/log_history.html')

@login_required
def about(request: HttpRequest) -> HttpResponse:
    """About page."""
    return render(request, 'dashboard/about.html')

@login_required
def inventory(request: HttpRequest) -> HttpResponse:
    """Inventory management page. This view now provides mock inventory data."""
    
    # Mock data structure matching the loop in inventory.html:
    # {% for item in inventory %} looks for item.name, item.category, item.stock, item.updated_at
    mock_inventory = [
        {'name': 'Strawberry Cake Base', 'category': 'Cakes', 'stock': 25, 'updated_at': '2025-10-13 10:00'},
        {'name': 'Chocolate Ganache', 'category': 'Toppings', 'stock': 5, 'updated_at': '2025-10-12 15:30'},
        {'name': 'Rainbow Sprinkles', 'category': 'Ingredients', 'stock': 0, 'updated_at': '2025-10-10 09:15'},
        {'name': 'Large Cake Boxes', 'category': 'Packaging', 'stock': 45, 'updated_at': '2025-10-13 11:20'},
    ]
    
    context = {
        'inventory': mock_inventory
    }
    
    # The view now passes the 'inventory' data to the template.
    return render(request, 'dashboard/inventory.html', context)
