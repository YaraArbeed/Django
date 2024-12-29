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
#----------------------Lecture10--------------------------------------------
class Author3(models.Model):
    fullname = models.CharField(max_length=100, null=False)  # Author's full name
    address = models.TextField(max_length=500, null=True)  # Optional address of the author
    
    def __str__(self): 
        return self.fullname  # Returns the author's name as a string representation
class Book3(models.Model):
    title = models.CharField(max_length=100, null=False)  # Title of the book
    price = models.FloatField(default=0)  # Price of the book, default is 0
    genre = models.CharField(max_length=50)  # Add the genre field here
    authors = models.ManyToManyField(Author3)  # Many-to-many relationship with the Author model
    coverPage = models.FileField(upload_to='documents/')  # or use ImageField for image-specific uploads

    
    def __str__(self): 
        return self.title  # Returns the title of the book as a string representation





