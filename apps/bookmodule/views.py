from django.shortcuts import render,redirect
from .models import Book

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
def list_books(request):
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