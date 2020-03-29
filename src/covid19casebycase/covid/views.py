from django.shortcuts import render
from django.http import HttpResponse
import json
import sys

# Create your views here.

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

def _getSymptomPercentageCountry(country_name, attribute_name, attribute_value):
    return 0.10

def getSymptomPercentageState(request):
    body = json.loads(request.body)
    return HttpResponse("Here is state %s percentage.")

def getSymptomPercentageCounty(request):
    body = json.loads(request.body)
    return HttpResponse("Here is county %s percentage.")
    