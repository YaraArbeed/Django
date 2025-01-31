from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,Student,Address,ExamBook,Author,Student2,Address2,Image
from django.db.models import Q
from django.db.models import Count,Sum, Avg, Max, Min
from .forms import BookForm,StudentForm, AddressForm,Student2Form, Address2Form,ImageForm,BookForm3
#--------------------AI project-------------------------------
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
#--------------------------------------------------------------
def index(request):
# render the appropriate template for this request
 return render(request, 'bookmodule/index.html')

def books2(request):
 return render(request, 'bookmodule/bookList2.html',{'books2':__getBooks()})

def books(request):
   return render(request,'bookmodule/bookList.html')

def filterbooks(request):
   if request.method == "POST":
    string = request.POST.get('keyword').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')

    selected=request.POST.get('selectedgenre')
    print(f"selected thing = {selected}")

    # now filter
    books = __getBooks()
    newBooks = []
    for item in books:
       contained = False
       if isTitle and string in item['title'].lower(): contained = True
       if not contained and isAuthor and string in item['author'].lower():contained = True
       if contained: newBooks.append(item)
    return render(request, 'bookmodule/bookList2.html', {'books2':newBooks})
   return render(request,'bookmodule/search.html',{})

def book(request,bId):
   book1={'id':12344321, 'title':'Continous Delivery','author':'J.Humble and D.Farley'}
   book2={'id':56788765, 'title':'Reversing: Secrut of Reverse Engineering','author':'E.Elim'}
   targetBook=None
   if book1['id']==bId:targetBook=book1
   if book2['id']==bId:targetBook=book2

   if targetBook==None: return redirect('/books')

   context={'book':targetBook} # book is the variable name accessible by template
   return render(request,'bookmodule/book.html',context)


def __getBooks():
   books=[]
   book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
   book2 = {'id':56788765, 'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
   book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
   books.append(book1)
   books.append(book2)
   books.append(book3)
   return books
#-----------------------Lab4-------------------------------------
def lab_index(request):
 return render(request, "bookmodule/CS471_Labs/index.html")
def list_books2(request):
 return render(request, 'bookmodule/CS471_Labs/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/CS471_Labs/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/CS471_Labs/aboutus.html')
#------------------------Lab5-----------------------------------
def html5_links(request):
    return render(request, 'bookmodule/CS471_Labs/links.html')
def html5_text_formatting(request):
    return render(request, 'bookmodule/CS471_Labs/formatting.html')
def html5_listing(request):
    return render(request, 'bookmodule/CS471_Labs/listing.html')
def html5_tables(request):
    return render(request, 'bookmodule/CS471_Labs/tables.html')
#-----------------------Lab6--------------------------------------#
def search(request):
 if request.method == "POST":
  string = request.POST.get('keyword').lower()
  isTitle = request.POST.get('option1')
  isAuthor = request.POST.get('option2')
  # now filter
  books = __getBooks()
  newBooks = []
  for item in books:
   contained = False
   if isTitle and string in item['title'].lower(): contained = True
   if not contained and isAuthor and string in item['author'].lower():contained = True

   if contained: newBooks.append(item)
  return render(request, 'bookmodule/bookList2.html', {'books2':newBooks})
 return render(request, 'bookmodule/CS471_Labs/search.html')
#-------------------------Lab7--------------------------------------
def simple_query(request):
  mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
  return render(request, 'bookmodule/bookList2.html', {'books2':mybooks})

def lookup_query(request):
 mybooks=books=Book.objects.filter(author__isnull = 
 False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
 if len(mybooks)>=1:
  return render(request, 'bookmodule/bookList2.html', {'books2':mybooks})
 else:
  return render(request, 'bookmodule/CS471_Labs/index.html')
#---------------------------AI project-----------------------------------
# Helper function to convert a plot to a PNG image
def plot_to_image():
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()
    return base64.b64encode(image_png).decode('utf-8')

def home(request):
    return render(request, 'bookmodule/home.html')

# Register mse if used as a shorthand
@tf.keras.utils.register_keras_serializable()
def mse(y_true, y_pred):
    return tf.keras.losses.mean_squared_error(y_true, y_pred)
# Load the pre-trained model (global loading to avoid repeated loading)
MODEL_PATH = r"C:\Users\yarax\Downloads\stacked_model.h5"

pretrained_model = tf.keras.models.load_model(
    MODEL_PATH,
    custom_objects={'mse': tf.keras.losses.MeanSquaredError}
)
def predict(request):
    if request.method == 'POST' and 'csv_file' in request.FILES:
        try:
            csv_file = request.FILES['csv_file']
            
            # Read the CSV file without headers
            data = pd.read_csv(csv_file, header=None)
            data.columns = ['Date', 'Consumption']  # Manually assign column names
            
            # Parse the 'Date' column as datetime, assuming day-first format
            data['Date'] = pd.to_datetime(data['Date'], format='%d-%b', errors='coerce')
            data = data.dropna(subset=['Date'])  # Drop rows where date parsing failed
            data.set_index('Date', inplace=True)
            
            # Resample to daily and then to hourly data
            daily_data = data.resample('D').interpolate(method='linear')
            hourly_data = daily_data.resample('H').interpolate(method='linear')

            # Normalize data
            scaler = MinMaxScaler()
            hourly_data['Consumption'] = scaler.fit_transform(hourly_data[['Consumption']])

            # Prepare sequences for LSTM
            sequence_length = 24
            X, y = [], []
            for i in range(len(hourly_data) - sequence_length):
                X.append(hourly_data['Consumption'].values[i:i + sequence_length])
                y.append(hourly_data['Consumption'].values[i + sequence_length])
            X = np.array(X).reshape((len(X), sequence_length, 1))
            y = np.array(y)

            # Use the pre-trained model for predictions
            predictions = pretrained_model.predict(X)
            predictions = scaler.inverse_transform(predictions)

            # Convert predictions and actual values to text format
            predictions_text = "\n".join([f"Predicted Consumption: {pred[0]:.2f}" for pred in predictions])

               # Plot only the predicted values
            plt.figure(figsize=(15, 8))  # Adjust the figure size as needed
            plt.plot(predictions, label='Predicted Consumption', color='orange')
            plt.title('Hourly Predicted Consumption')
            plt.xlabel('Time (Hours)')
            plt.ylabel('Predicted Consumption')
            plt.grid(True)  # Optional: Adds a grid to the background for better readability
            plt.legend().remove()
            image = plot_to_image()

        

            # Render results on a webpage
            return render(request, 'bookmodule/predict.html', {'plot': image, 'predictions_text': predictions_text})

        except Exception as e:
            print("Error during prediction:", e)
            return render(request, 'bookmodule/home.html', {'error': str(e)})

    return render(request, 'bookmodule/home.html')
#--------------------------------Lab8--------------------------
def lab8_task1(request):
    # Query to fetch books with price <= 50
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/CS471_Labs/lab8_task1.html', {'books': books})

def lab8_task2(request):
    #Use Q operators to filter the books
    books =  Book.objects.filter(
        Q(edition__gt=2) & 
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/CS471_Labs/lab8_task2.html', {'books': books})

def lab8_task3(request):
    #Use ~Q operators to filter the books
    books =  Book.objects.filter(
        ~Q(edition__gt=2) & 
        (~Q(title__icontains='qu') | ~Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/CS471_Labs/lab8_task3.html', {'books': books})

def lab8_task4(request):
    # Retrieve books and order them by title
    books = Book.objects.order_by('title')
    print(books) 
    # Render the results to an HTML template
    return render(request, 'bookmodule/CS471_Labs/lab8_task4.html', {'books': books})

def lab8_task5(request):
    # Perform aggregation
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price', default=0),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    # Pass the aggregated data to the template
    return render(request, 'bookmodule/CS471_Labs/lab8_task5.html', {'stats': stats})

def lab8_task7(request):
    # Annotate students by city and count the number of students in each city
    students_per_city = Student.objects.values('address__city').annotate(num_students=Count('id')).order_by('address__city')

    # Render the results to the HTML template
    return render(request, 'bookmodule/CS471_Labs/lab8_task7.html', {'students_per_city': students_per_city})
#------------------------------Revision------------------------------------
def revision_task1(request):
    return render(request, 'bookmodule/CS471_Labs/revision_task1.html')

def revision_task2(request):
    books = ExamBook.objects.select_related('Author').all()
    return render(request, 'bookmodule/CS471_Labs/revision_task2.html', {'books': books})

def revision_task3(request, book_id):
    book = get_object_or_404(ExamBook, id=book_id)
    return render(request, 'bookmodule/CS471_Labs/revision_task3.html', {'book': book})
#------------------------------Lab9---------------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/CS471_Labs/list-books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        author = request.POST.get('author')
        if title and price and edition and author:
            Book.objects.create(title=title, price=float(price), edition=int(edition), author=author)
            return redirect('list_books')
    return render(request, 'bookmodule/CS471_Labs/add_book.html')

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.price = float(request.POST.get('price', book.price))  # Convert to float
        book.edition = int(request.POST.get('edition', book.edition))  # Convert to int
        book.author = request.POST.get('author', book.author)
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/CS471_Labs/edit_book.html', {'book': book})



def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')
#----------------------------------------------------------------
# List books
def list_books_form(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/CS471_Labs/list-book-form.html', {'books': books})

# Add a new book
def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm()
    return render(request, 'bookmodule/CS471_Labs/add-book-form.html', {'form': form})

# Edit a book
def edit_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/CS471_Labs/edit-book-form.html', {'form': form})

# Delete a book
def delete_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_form')
    return render(request, 'bookmodule/CS471_Labs/delete-book-form.html', {'book': book})
#-------------------------Lab10--------------------------------------------
def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/CS471_Labs/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('list_students')
    else:
        student_form = StudentForm()
    return render(request, 'bookmodule/CS471_Labs/add_student.html', {'form': student_form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('list_students')
    else:
        student_form = StudentForm(instance=student)
    return render(request, 'bookmodule/CS471_Labs/edit_student.html', {'form': student_form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('list_students')
#----------------------------------------------------
def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/CS471_Labs/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        student_form = Student2Form(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('list_students')
    else:
        student_form = Student2Form()
    return render(request, 'bookmodule/CS471_Labs/add_student.html', {'form': student_form})

def edit_student2(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        student_form = Student2Form(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('list_students')
    else:
        student_form = Student2Form(instance=student)
    return render(request, 'bookmodule/CS471_Labs/edit_student.html', {'form': student_form})

def delete_student2(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    student.delete()
    return redirect('list_students')

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = ImageForm()
    return render(request, 'bookmodule/CS471_Labs/upload_image.html', {'form': form})

def list_images(request):
    images = Image.objects.all()
    return render(request, 'bookmodule/CS471_Labs/list_images.html', {'images': images})
#----------------------Lecture 9--------------------------------------

#create book,update
'''
def addBook(request):
    if request.method=='POST':
        titleval=request.POST.get('title')
        authorval=request.POST.get('author')
        priceval=request.POST.get('price')
        editionval=request.POST.get('edition')
        obj=Book(title=titleval,author=authorval,price=priceval,edition=editionval)
        obj.save()
        return redirect('readBook',bId=obj.id)
    return render(request,'bookmodule/addBook.html',{})
'''
def addBook(request):
    obj = None
    authors = Author.objects.all().order_by('Name')
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('readBook', bId = obj.id)
    else: form = BookForm(None)
    return render(request, "bookmodule/addBook.html", {'authors':authors, 'form':form})

def updateBook(request,bId):
    obj=Book.objects.get(id=bId)
    if request.method=='POST':
        form = BookForm(request.POST,instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('readBook', bId = obj.id)
    form = BookForm(instance=obj)
    return render(request, "bookmodule/addBook.html", {'form':form})

'''
def updateBook(request,bId):
    obj=Book.objects.get(id=bId)
    if request.method=='POST':
        titleval=request.POST.get('title')
        authorval=request.POST.get('author')
        priceval=request.POST.get('price')
        editionval=request.POST.get('edition')
        obj.title=titleval
        obj.author=authorval
        obj.price=priceval
        obj.edition=editionval
        obj.save()
        return redirect('readBook',bId=obj.id)
    return render(request,"bookmodule/updateBook.html", {'obj':obj})
'''
def listBooks(request):
    books=Book.objects.all()
    return render(request,'bookmodule/bookList2.html',{'books':books})

def readBook(request,bId):#same as show/display
    obj=Book.objects.all().get(id=bId)
    return render(request,'bookmodule/book.html',{'book':obj})

def deleteBook(request, bId):
    # Retrieve the book object with the given ID
    obj = Book.objects.get(id=bId)
    
    if request.method == 'POST':
        # Delete the book object
        obj.delete()
        # Redirect to the list of books after deletion
        return redirect('listBooks')
    
    # Render the delete confirmation page
    return render(request, "bookmodule/deleteBook.html", {'obj': obj})
#---------------------------------Lecture10-----------------------------
def addBook3(request):
    if request.method == 'POST':
        form = BookForm3(request.POST,request.FILES)
        if form.is_valid():
            price = form.cleaned_data['price']  # Access the cleaned price data from the form
            print(f"Price is equal to: {price}")  # Print the price (or use it in your logic)
            form.save()
            return redirect('index')
        print(form.errors)  # Print form errors to debug
    form = BookForm3(None)
    return render(request, 'bookmodule/addBook3.html', {'form':form})


