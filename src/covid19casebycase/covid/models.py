from django.db import models

#Location Models 
class Case(models.Model): 

    GENDERS_AVAILABLE = [
        ("female","female"),
        ("male","male")
    ]
    age = models.IntegerField(null=True) 
    gender = models.CharField(max_length=10,choices=GENDERS_AVAILABLE)
    country = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    death = models.BooleanField(default=False) 
    recovered = models.BooleanField(default=False)
    

    

class Symptom(models.Model): 

    class Meta: 
        unique_together = ("case","name") #symptom name and case should be unique together

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 





