from django.db import models
from django.apps import apps

#Model Managers 
class UniqueManager(models.Manager): 
    def get_unique(self,field=None): 
        return [model.get(field) for model in self.all().order_by(field).values(field).distinct()]

class CaseManager(UniqueManager): 
    def get_queryset(self):
        return CaseQuerySet(self.model)

class CaseQuerySet(models.QuerySet):
    related_attribute_map = {
    "symptom": 
        {
            "model_name": "Symptom",
            "field": "name"
        }
    }
    

    available_attributes_case = ["age", "gender", "country"]
    available_attributes_related = [key for key in related_attribute_map]

    available_attributes = available_attributes_case + available_attributes_related 

    
    def filter_by_attribute(self, attribute_name, attribute_value, additional_args={}):
        if attribute_name not in self.available_attributes: 
            return self

        if attribute_name in self.available_attributes_case: 
            lint_field, casted_value = self.cast_for_query(Case, attribute_name, attribute_value)
            if(attribute_name == "age") and additional_args.get("span"): 
                span = additional_args.get("span")
                return self.filter(age__gte=casted_value-span, age__lte=casted_value+span)
            else:      
                return self.filter(**{lint_field: casted_value})

        elif attribute_name in self.available_attributes_related: 
            related_object_map = self.related_attribute_map.get(attribute_name)
            model = apps.get_model('covid', related_object_map.get("model_name"))
            field = related_object_map.get("field")
            lint_field, casted_value = self.cast_for_query(model, field, attribute_value)
            object_list = model.objects.filter(**{lint_field: casted_value})
            return self.filter(pk__in=list(object_list.values_list("case__pk", flat=True)))     
        return self
    
    def cast_for_query(self, model, field, value): 
        casted_value =  model._meta.get_field(field).to_python(value) 
        if(type(casted_value)==str): 
            field = field+"__iexact"
        return field, casted_value


#Location Models 
class Case(models.Model): 

    GENDERS_AVAILABLE = [
        ("female","female"),
        ("male","male")
    ]

    objects = CaseManager()

    age = models.IntegerField(null=True) 
    gender = models.CharField(max_length=10,choices=GENDERS_AVAILABLE)
    country = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    death = models.BooleanField(default=False) 
    recovered = models.BooleanField(default=False)
       
class Symptom(models.Model): 

    class Meta: 
        unique_together = ("case","name") #symptom name and case should be unique together

    objects = UniqueManager() 

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
