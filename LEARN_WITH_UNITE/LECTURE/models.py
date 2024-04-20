from django.db import models
from django.utils import timezone
from django.urls import reverse

# the post class is connected to the superuser 

###########################################################

class Biology_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Biology5Tutorial(models.Model):
    topic = models.ForeignKey(Biology_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################

##############################################################

class Chemistry_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chemistry5Tutorial(models.Model):
    topic = models.ForeignKey(Chemistry_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################

##############################################################

class Economics_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Economics5Tutorial(models.Model):
    topic = models.ForeignKey(Economics_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################

##############################################################

class English_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class English5Tutorial(models.Model):
    topic = models.ForeignKey(English_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################


##############################################################

class Geography_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Geography5Tutorial(models.Model):
    topic = models.ForeignKey(Geography_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################

##############################################################

class History_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class History5Tutorial(models.Model):
    topic = models.ForeignKey(History_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################


##############################################################

class Kiswahili_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kiswahili5Tutorial(models.Model):
    topic = models.ForeignKey(Kiswahili_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################


##############################################################

class Mathematics_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mathematics5Tutorial(models.Model):
    topic = models.ForeignKey(Mathematics_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################

class Physics_Form5(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Physics5Tutorial(models.Model):
    topic = models.ForeignKey(Physics_Form5, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/%Y/%m/%d')

    def __str__(self):
        return self.title
    
###############################################################


