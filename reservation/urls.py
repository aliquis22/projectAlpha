from django.urls import path
from . import views
from .views import home, reservation, user_organisations, org_profile


urlpatterns = [
	path('', views.home, name='index'),
	path('about/', views.about, name='about'),
	path('organisation/<int:pk>/reservation', reservation, name='reservation'),
	path('user_organisations/', user_organisations, name='user_organisations'),
	path('user_organisations/organisation/<int:organisation_id>', org_profile, name='org_profile'),

]