from django.shortcuts import render
from django.http import HttpResponse
import json
import sys
from .models import Case,Symptom

# Create your views here.

def _getSymptomPercentageCountry(country_name, attribute_name, attribute_value):
    return 0.10



def getSymptomPercentageCountry(request):
    body = json.loads(request.body)
    resp_dict = {}

    location = body["location"]
    attributes = body["attributes"]

    resp_dict["country"] = location
    resp_dict["attributePercentages"] = {}

    for field in attributes:
        percentage = _getSymptomPercentageCountry(location, field, attributes[field])
        resp_dict["attributePercentages"][field] = percentage

    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)

def _getSymptomPercentageState(state_name, attribute_name, attribute_value):
    return 0.20

def getSymptomPercentageState(request):
    body = json.loads(request.body)
    resp_dict = {}

    location = body["location"]
    attributes = body["attributes"]

    resp_dict["state"] = location
    resp_dict["attributePercentages"] = {}

    for field in attributes:
        percentage = _getSymptomPercentageState(location, field, attributes[field])
        resp_dict["attributePercentages"][field] = percentage

    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)

def _getSymptomPercentageCounty(county_name, attribute_name, attribute_value):
    return 0.30

def getSymptomPercentageCounty(request):
    body = json.loads(request.body)
    resp_dict = {}

    location = body["location"]
    attributes = body["attributes"]

    resp_dict["county"] = location
    resp_dict["attributePercentages"] = {}

    for field in attributes:
        percentage = _getSymptomPercentageCounty(location, field, attributes[field])
        resp_dict["attributePercentages"][field] = percentage

    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)
    
def getSymptoms(request):
    resp_dict = {}

    resp_dict["symptoms"] = _getSymptoms()
    
    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)

def _getSymptoms():
    return list(Symptom.objects.order_by("name").values_list("name", flat=True).distinct()) 


def getCountries(request):
    resp_dict = {}

    resp_dict["countries"] = _getCountries()

    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)



def _getCountries():
    return  list(Case.objects.order_by("country").values_list('country', flat=True).distinct())

def getStates(request):
    resp_dict = {}

    resp_dict["states"] = _getStates()

    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)

def _getStates():
    states = []
    states.append("wurshingtun")
    states.append("kanto")

    return states

def getCounties(request):
    resp_dict = {}

    resp_dict["counties"] = _getCounties()

    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)

def _getCounties():
    counties = []
    counties.append("king")
    counties.append("queen")
    counties.append("pallet town")

    return counties

def updateDB(request): 
    from .parser import parseKaggleCSV

    parseKaggleCSV()