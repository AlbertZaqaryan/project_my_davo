from django.db import models

# Create your models here.

class Notebook(models.Model):

    name = models.CharField('Notebook name', max_length=60)
    price = models.PositiveIntegerField('Notebook price')
    img = models.ImageField('Notebook image', upload_to='images')
    about = models.TextField('Notebook text')

    def __str__(self):
        return self.name
    

class Review(models.Model):

    email = models.EmailField('Review user email')
    phone = models.CharField('Review user phone number', max_length=100)
    text = models.TextField('Review user text')

    def __str__(self):
        return self.email