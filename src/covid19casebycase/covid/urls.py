from django.urls import path

from . import views

urlpatterns = [
    path('getSymptomPercentageCountry', views.getSymptomPercentageCountry, name='getSymptomPercentageCountry'),
    path('getSymptomPercentageState', views.getSymptomPercentageState, name='getSymptomPercentageState'),
    path('getSymptomPercentage', views.getSymptomPercentageCounty, name='getSymptomPercentageCounty'),
]