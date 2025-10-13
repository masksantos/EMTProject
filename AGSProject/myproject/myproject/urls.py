from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from dashboard.views import login_view, logout_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),  # Home page/dashboard
    path('dashboard/', include('dashboard.urls')),  # if you have other dashboard routes
=======
from dashboard import views as dashboard_views  # ✅ import your dashboard views
from accounts import views as accounts_views    # keep this if you have login/logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),

    # ✅ Home URLs — now pointing to dashboard views
    path('', dashboard_views.home, name='home'),
    path('home/', dashboard_views.home, name='home_page'),

    # ✅ Include dashboard URLs
    path('', include('dashboard.urls')),
>>>>>>> 3f2e4059f08fe8e95e55caf3cf6cbf639dacf92b
]
