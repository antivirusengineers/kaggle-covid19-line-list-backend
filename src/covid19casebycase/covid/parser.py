import csv 
from django.conf import settings
from .models import Case,Symptom

def parseKaggleCSV(): 
    #delete all previous values in the database. 
    Case.objects.all().delete() 
    #now read and populate database from CSV. 
    with open(settings.KAGGLE_CSV_FILE, newline='',errors='ignore') as csvfile:
        kagglereader = csv.reader(csvfile)
        headers = next(kagglereader, None)
        indices = {} 
        headers_required = ["age","gender", "country","symptom","death","recovered","location"]
        for name in headers_required: 
            indices[name]=headers.index(name)

        for row in kagglereader: 
            #create a new case 
            case = Case() 
            try: 
                case.age = int(row[indices["age"]])
            except: 
                pass

            case.gender = row[indices["gender"]]
            case.country = row[indices["country"]]
            case.location = row[indices["location"]]
            try: 
                case.death = bool(int(row[indices["death"]])) 
            except: 
                pass 
            try: 
                case.recovered = bool(int(row[indices["recovered"]])) 
            except: 
                pass
            case.save() #this saves the case to the database.

            #now parse the symptomology for the case
            for symptom_name in row[indices["symptom"]].split(","): 
                symptom = Symptom(case = case)
                symptom.name=symptom_name
                symptom.save()

        
            

