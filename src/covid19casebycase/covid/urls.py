from django.urls import path

from . import views

urlpatterns = [
    path('prevalence', views.Prevalence.as_view(), name='prevalence'),
    path('symptom-list', views.ListSymptoms.as_view(), name='symptom-list'),
    path('country-list', views.ListCountries.as_view(), name='country-list'),
    path('gender-list', views.ListGenders.as_view(), name="gender-list"),
    path('updateDB', views.updateDB, name='UpdateDB') #this is for testing. should not be removed from prod.
]