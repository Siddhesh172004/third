from django.db import models


# Create your models here.

class Mens(models.Model):
    
    mens_id = models.AutoField
    title =  models.CharField(max_length=50)
    oldprice = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="Home\mensimg\images",default="")
   
    
    def __str__(self):
        return self.title
