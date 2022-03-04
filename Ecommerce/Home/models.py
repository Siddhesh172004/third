from django.db import models

# Create your models here.
class Mens(models.Model):
    
    mens_id = models.AutoField
    title =  models.CharField(max_length=50)
    Sale_or_not =  models.CharField(max_length=50,default="No Sale")
    price = models.FloatField()
    image = models.ImageField(upload_to="Home\mensimg\images",default="")
    descriptions= models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.title

class Womens(models.Model):
    
    womens_id = models.AutoField
    title =  models.CharField(max_length=50)
    Sale_or_not =  models.CharField(max_length=50,default="No Sale")
    price = models.FloatField()
    image = models.ImageField(upload_to="Home\womensimg\images",default="")
    descriptions= models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.title

class Kids(models.Model):
    
    kids_id = models.AutoField
    title =  models.CharField(max_length=50)
    Sale_or_not =  models.CharField(max_length=50,default="No Sale")
    price = models.FloatField()
    image = models.ImageField(upload_to="Home\kidsimg\images",default="")
    descriptions= models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.title

class Accessories(models.Model):
    
    Accessories_id = models.AutoField
    title =  models.CharField(max_length=50)
    Sale_or_not =  models.CharField(max_length=50,default="No Sale")
    price = models.FloatField()
    image = models.ImageField(upload_to="Home\ccessories\images",default="")
    descriptions= models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.title
