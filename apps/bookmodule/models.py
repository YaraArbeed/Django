from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)
    author = models.CharField(max_length = 50)
 #--------------------Lab8-Task6--------------------------   
class Address(models.Model):
    city = models.CharField(max_length=100)
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
#--------------------Revision------------------------------------
class Author (models.Model):
  Name=models.CharField(max_length=100) 
                         
class ExamBook(models.Model):
    Title=models.CharField(max_length=100)
    Author=models.ForeignKey(Author, on_delete=models.CASCADE)
#---------------------Lab10 Task2--------------------------------------
class Address2(models.Model):
    city = models.CharField(max_length=100)

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    addresses = models.ManyToManyField(Address2)
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title



