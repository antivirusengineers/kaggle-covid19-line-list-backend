import csv 
from django.conf import settings
from .models import Case,Symptom

<<<<<<< HEAD
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

        
            

=======
class ParserBaseClass(): 
    #supported key map has the format (dict_key,type, model, field)
    supported_key_map_case = [
        {"key":"age",
        "type": int,
        "model": Case, 
        "field": "age"},
        {"key":"gender",
        "type": str,
        "model": Case, 
        "field": "gender"},
        {"key":"country",
        "type": str,
        "model": Case, 
        "field": "country"},
        {"key":"death",
        "type": bool,
        "model": Case, 
        "field": "death"},
        {"key":"recovered",
        "type": bool,
        "model": Case, 
        "field": "recovered"}
    ]

    supported_key_map_case_related = [
        {"key":"symptom_list",
        "type": list,
        "list_type": str,
        "model": Symptom, 
        "field": "name"}
    ] 

    supported_key_map = supported_key_map_case + supported_key_map_case_related

    def getSupportedHeaders(self): 
        return [row["key"] for row in self.supported_key_map]

    def getSupportedHeadersWithType(self): 
        return [(row["key"],row["type"]) for row in self.supported_key_map]

    def saveListOfCases(self, case_list): 
        for case in case_list: 
            self.parseDict(case)

    def create_related_object_helper(self, model, field, valtype, value, case): 
        related_object = model() 
        related_object.case = case 
        setattr(related_object, field, valtype(value))
        related_object.save() 

    def parseDict(self, case_dict): 
        #Create a new Case entry for this ditionary: 
        case = Case() 
        for row in self.supported_key_map_case: 
            try: 
                linted_value = case_dict[row["key"]]
                if(row["type"]==bool): 
                    linted_value = int(case_dict[row["key"]])

                value = row["type"](linted_value) 
                setattr(case, row["field"], value)
            except: 
                pass
        case.save() 

        #Now we add all related objects to case (note this only supports related objects as single row): 
        for row in self.supported_key_map_case_related: 
            if(row["type"]==list): 
                for item in case_dict[row["key"]].split(","): 
                    self.create_related_object_helper(row["model"], row["field"], row["list_type"], item, case)
            else: 
                self.create_related_object_helper(row["model"], row["field"], row["type"], case_dict["key"], case)
                      

        
class CSVParser(ParserBaseClass): 
    reader = None 
    header_map = None 
    index_map = None

    def getHeaderToKeyMap(self): 
        header_map = {}
        for header in self.getSupportedHeaders(): 
            header_map[header] = header 
        return header_map
    
    def getHeaderToIndexMap(self,csv_headers): 
        index_map = {}
        for key,val in self.getHeaderToKeyMap().items(): 
            index_map[val]=csv_headers.index(val)
        return index_map

    def createCaseDictFromRow(self, row, header_map, index_map): 
        case_dict = {}
        for case_header,csv_header in header_map.items(): 
            case_dict[case_header] = row[index_map[csv_header]]
        return case_dict

    def getCaseListFromReader(self, reader, csv_headers): 
        header_map = self.getHeaderToKeyMap()
        index_map = self.getHeaderToIndexMap(csv_headers) 
        case_list = []
        for row in reader: 
            try: 
                case_list.append(self.createCaseDictFromRow(row, header_map, index_map))
            except Exception as e: 
                print(e)
        return case_list
    
    def FillDatabaseFromReader(self, reader, csv_headers): 
        case_list = self.getCaseListFromReader(reader, csv_headers)
        self.saveListOfCases(case_list)

class KaggleCSVParser(CSVParser): 

    def getHeaderToKeyMap(self): 
        header_map = super().getHeaderToKeyMap() 
        header_map["symptom_list"] = "symptom"
        return header_map

    def parse(self, filename=None): 
        #delete all previous values in the database. 
        Case.objects.all().delete() 
        #now read and populate database from CSV. 
        case_list = [] 

        if not filename: 
            filename=settings.KAGGLE_LOCAL_FILENAME

        with open(filename, newline='',errors='ignore') as csvfile:
            kagglereader = csv.reader(csvfile)
            csv_headers = next(kagglereader, None)
            self.FillDatabaseFromReader(kagglereader, csv_headers)





       
>>>>>>> 9195e7d2bb94af7e2ce1b01b2358a70bb71af2ee
