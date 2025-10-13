from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html')

def inventory(request):
    return render(request, 'dashboard/inventory.html')

def notifications(request):
    return render(request, 'dashboard/notifications.html')

def log_history(request):
    return render(request, 'dashboard/log_history.html')

def about(request):
    return render(request, 'dashboard/about.html')

def flavors(request):
    # Example context, replace with your actual data
    context = {}
    return render(request, 'dashboard/flavors.html', context)

def ingredients(request):
    return render(request, 'dashboard/ingredients.html')

def toppings(request):
    return render(request, 'dashboard/toppings.html')

def packaging(request):
    return render(request, 'dashboard/packaging.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home/dashboard page
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'dashboard/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Example home/dashboard view
def home_view(request):
    return render(request, 'dashboard/home.html')