from django.db import models

# Create your models here.

class Creator(models.Model):
    
    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.first_name
        
class Language(models.Model):
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
class Frameworks(models.Model):
    name = models.CharField(max_length=40)
    dil = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 
