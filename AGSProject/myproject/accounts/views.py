from django.shortcuts import render

def dashboard_home(request):
    return render(request, 'dashboard/home.html')

def reports(request):
    return render(request, 'dashboard/reports.html')

<<<<<<< HEAD
def settings(request):
    return render(request, 'dashboard/settings.html')
=======
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    logs = [
        {"date": "09-29-25", "product_name": "Sprinkles", "status": "Low", "action": "For Restock", "staff": "Staff Jane"},
    ] 
>>>>>>> 3f2e4059f08fe8e95e55caf3cf6cbf639dacf92b
