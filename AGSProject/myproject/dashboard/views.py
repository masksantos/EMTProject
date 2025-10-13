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
