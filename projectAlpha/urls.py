from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from registration import views as reg_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reservation/',include('reservation.urls')),
    path('register/',reg_views.register, name = 'register'),
    path('', RedirectView.as_view(url='/reservation/home/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)