from django.shortcuts import render
from django.http import HttpResponse
import json
import sys
from .models import Case,Symptom
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ListSymptoms(APIView):
    def get(self, request, format=None):
        symptoms = Symptom.objects.get_unique("name")
        return Response(symptoms)

class ListCountries(APIView):
    def get(self, request, format=None):
        countries = Case.objects.get_unique("country")
        return Response(countries)

class ListGenders(APIView):
    def get(self, request, format=None):
        genders = [x for (x,y) in Case.GENDERS_AVAILABLE] 
        return Response(genders)

class Prevalence(APIView): 
    prevalence_tiers = ["country"]

    def get(self, request, format=None): 
        """ 
        REQUEST FORMAT: 
        {"attributes": 
            {
                "attr_name": val, 
                "attr_name_list": [list_of_vals]
            }, 
        "additional_args": {
            "attr_name" (relates to above list): 
                {
                    "additional_arg": val 
                }
            }
        "localization": "val"
        }

        SUPPORTED ATTRIBUTES: 
        "age", "gender", "symptom_list", "country" 

        SUPPORTED ADDITIONAL ARGUMENTS: 
        "age" --> "span" 

        SUPPORTED LOCALIZATION: 
        "country" 

        """
        attributes = request.data.get("attributes") 

        #if there are no attributes, do not proceed with calculations. Nothing to determine.
        if not attributes: 
            return Response(
                status=400
            )
        attributes = json.loads(attributes)

        additional_args =request.data.get("additional_args")

        additional_args = json.loads(additional_args) if additional_args else {}
        #not yet supported - this will allow users to determine the level of localization for 
        #percentage calculations - i.e. State level, country level etc. 
        localization = request.data.get("localization") 
        #for now it will always be localized to country if available.
        localization = "country"

        cases = self.get_cases(attributes, additional_args)
        
        percentage = self.calculate_percentage(cases,attributes.get(localization), localization)

        return Response(
            { 
                "percentage": percentage
            }
        )

    def calculate_percentage(self, cases, location=None, location_type = "country"): 
        if location: 
            return cases.count()/Case.objects.filter(**{location_type: location}).count() 
        else: 
            return cases.count()/Case.objects.all().count()

    def get_cases(self, attributes, additional_args={}): 
        cases = Case.objects.all() 
        
        for field in attributes: 
            value = attributes[field]
            args = additional_args.get(field)
            if type(value) is list: 
                filter_field = field[:-5]
                for single_value in value: 
                    if type(single_value)==str: 
                        single_value=single_value.strip()
                    cases = cases.filter_by_attribute(filter_field, single_value, args if args else {})
            else: 
                if type(value)==str: 
                    value = value.strip()
                cases = cases.filter_by_attribute(field, value, args if args else {})  
        
        return cases

def updateDB(request):  
    from .cron import refreshKaggleDataset 
    refreshKaggleDataset() 
