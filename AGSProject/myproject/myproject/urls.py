from django.contrib import admin
from django.urls import path, include
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
]
