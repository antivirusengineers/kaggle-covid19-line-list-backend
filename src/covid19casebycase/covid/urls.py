from django.urls import path

from . import views

urlpatterns = [
    path('getSymptomPercentageCountry', views.getSymptomPercentageCountry, name='getSymptomPercentageCountry'),
    path('getSymptomPercentageState', views.getSymptomPercentageState, name='getSymptomPercentageState'),
    path('getSymptomPercentage', views.getSymptomPercentageCounty, name='getSymptomPercentageCounty'),
    path('getSymptoms', views.getSymptoms, name='getSymptoms'),
    path('getCountries', views.getCountries, name='getCountries'),
    path('getStates', views.getStates, name='GetStates'),
    path('getCounties', views.getCounties, name='GetCounties'),
]