from django import forms
from .models import Book,Address,Student,Student2,Address2,Image
#------------------------------------Lab9-------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'edition', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'edition': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
#-----------------------------Lab10-----------------------------------
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
        
class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image', 'description']