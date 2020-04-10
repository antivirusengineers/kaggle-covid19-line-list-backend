from django.urls import path

from . import views

urlpatterns = [
    path('getSymptomPercentageCountry', views.getSymptomPercentageCountry, name='getSymptomPercentageCountry'),
    path('getSymptoms', views.getSymptoms, name='getSymptoms'),
    path('getCountries', views.getCountries, name='getCountries'),
    path('getGenders', views.getGenders, name="GetGenders"),
    path('updateDB', views.updateDB, name='UpdateDB') #this is for testing. should not be removed from prod.
]