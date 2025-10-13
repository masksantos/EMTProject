from django.shortcuts import render

def dashboard_home(request):
    return render(request, 'dashboard/home.html')

def reports(request):
    return render(request, 'dashboard/reports.html')

def settings(request):
    return render(request, 'dashboard/settings.html')
