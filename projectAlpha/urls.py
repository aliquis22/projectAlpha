from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from registration import views as reg_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservation.urls')),
    path('reservation/',include('reservation.urls')),
    path('register/',reg_views.register, name = 'register'),
    path('register_org/',reg_views.register_org, name = 'reg_org'),
    path('profile/', reg_views.profile, name='profile'),
    path('login/', reg_views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', RedirectView.as_view(url='/reservation/home/', permanent=True)),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)