from django import forms
from .models import Book,Address,Student,Student2,Address2,Image,Book3,Author3
#------------------------------------Lab9&Lec9-------------------------
class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'edition', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'edition': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
class BookForm(forms.ModelForm):
        class Meta: 
            model = Book
            fields = ['title', 'price', 'edition', 'author']
        
        title = forms.CharField(
            max_length=100,
            required=True,
            label="Title",
            widget= forms.TextInput(
                attrs= {
                    'placeholder':'Enter the title here',
                    'class':"mycssclass",
                    'id':'jsID'
                }
            )
        )
        author = forms.CharField(
            required=True,
            label="Author full name",
            max_length=100,
        )
        price = forms.DecimalField(
            required=True,
            label="Price",
            initial=0,
            min_value=1,
            max_value=100,
        )
        
        edition = forms.IntegerField(
            required=True,
            initial=0,
            label="Edition",
            widget=forms.NumberInput()
        )
#------------------------------Lec10----------------------------------
GENRE = ( ("fiction","Fiction"), ("mystrery","Mystrery"), ("fantasy","Fantasy"), ("biography","Biography") )

class BookForm3(forms.ModelForm):
    class Meta:
        model = Book3
        fields = '__all__'
    title = forms.CharField(label="Title", required=True)
    price = forms.FloatField(label="Price (with decimal point)",
    required=True,
    initial=0.00

)
    genre = forms.ChoiceField(label="Genre", choices=GENRE, 
        widget=forms.RadioSelect())

    authors = forms.ModelMultipleChoiceField(
    label="Authors",
    queryset=Author3.objects.all().order_by("fullname"),
    widget=forms.CheckboxSelectMultiple()
)

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