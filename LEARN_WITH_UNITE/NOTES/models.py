from django.db import models

# Create your models here.
      
class Biology_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title
    
class Chemistry_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

class Economics_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

    
class General_Studies_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

    
class Geography_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title


class History_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title
    
   
class Kiswahili_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title
 

class Language_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title
    
    
class Mathematics_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

class Physics_Form5(models.Model):
    picture = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    notes = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title
