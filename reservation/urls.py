from django.urls import path
from . import views
from .views import home, reservation


urlpatterns = [
	path('', views.home, name='index'),
	path('about/', views.about, name='about'),
	path('organisation/<int:pk>/reservation', reservation, name='reservation'),

]