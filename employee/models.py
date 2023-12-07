from django.db import models  
class Employee(models.Model):  
      
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)   
    eid = models.CharField(max_length=15) 
    

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee" 

class plant(models.Model):
    plantType = models.CharField(max_length=100)  
    photo = models.ImageField(upload_to='images/') 
    path = models.CharField(max_length=255)   
    time = models.CharField(max_length=255)
    
    def __str__(self):
        return self.plantType
    
    class Meta:  
        db_table = "plant"

class image(models.Model):
    path = models.URLField() 
    plantType = models.CharField(max_length=100)