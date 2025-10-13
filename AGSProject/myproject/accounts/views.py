from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

def login_view(request: HttpRequest) -> HttpResponse:
    """Handles user login."""
    if request.method == "POST":
        # Using .get() is safer than direct indexing
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to the dashboard home page (name='home' defined in dashboard/urls.py)
            return redirect('home') 
        else:
            # Display error message on failure
            messages.error(request, "Invalid username or password")
    
    # Render the login form page
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    """Handles user logout."""
    logout(request)
    # Redirect back to the login page (name='login' defined in accounts/urls.py)
    return redirect('login') 