from django.shortcuts import render
from django.http import HttpResponse
import json
import sys
from .models import Case,Symptom

# Create your views here.

def _getCasesForCountryAndAttribute(country_name, attribute_name, attribute_value,case_list=None):
    if not(case_list): 
        case_list = Case.objects.all() 
    if(attribute_name=="symptom"): 
        symptom_list = Symptom.objects.filter(name=attribute_value).values("case").distinct()
        cases = case_list.filter(pk__in=list(symptom_list.values_list("case__pk", flat=True)))
    elif(attribute_name=="age"): 
        cases = case_list.filter(age=int(attribute_value))
    elif(attribute_name=="gender"): 
        cases = case_list.filter(gender=attribute_value)
    
    if country_name: 
        return cases.filter(country=country_name)
    else: 
        return cases 



def _getSymptomPercentageCountry(country_name, attribute_name, attribute_value):
    cases = _getCasesForCountryAndAttribute(country_name,attribute_name,attribute_value)
    total_cases = getTotalCaseCount(country_name)
    return cases.count()/total_cases

def getTotalCaseCount(country_name=None): 
    if country_name: 
        return Case.objects.filter(country=country_name).count() 
    else: 
        return Case.objects.all().count()

def getSymptomPercentageCountry(request):

    resp_dict = {}

    location = request.GET.get("location")
    attributes = json.loads(request.GET.get("attributes"))
    print(location)
    print(attributes)
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
 
    resp_dict = {}

    location = request.GET.get("location")
   
    attributes = request.GET.get("attributes")

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

def getGenders(request): 
    resp_dict = {}

    resp_dict["genders"] = _getGenders()

    resp_body = json.dumps(resp_dict)
    return HttpResponse(resp_body)

def _getGenders(): 
    return [x for (x,y) in Case.GENDERS_AVAILABLE] 

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
    from .tasks import refreshKaggleDataset 
    refreshKaggleDataset() 