from django.shortcuts import render,redirect
from django.http import HttpResponse
#def index(request):
# render the appropriate template for this request
 #return render(request, 'bookmodule/index.html')

#lab work -task 1
#def index(request):
 #return HttpResponse("Hello, world!")

#lab work -task 2
#def index(request):
 #name = request.GET.get("name") or "world!" #add this line
 #return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name

#lab work -task4(update task 2)
#def index(request):
  #name = request.GET.get("name") or "world!"
  #return render(request, "bookmodule/index.html") #Change HttpResponse to render function

#lab work -task-5(update task 5)
def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, "bookmodule/index.html" , {"name": name}) #your render line

#lab work-task3
def index2(request, val1 = 0): #add the view function (index2)
  try:
    val1 = int(val1)
    return HttpResponse(f"value1 = {val1}")
  except ValueError:
     return HttpResponse("error, expected val1 to be integer")

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)

def books(request):
# render the appropriate template for this request
 return render(request, 'bookmodule/bookList.html') 
#using redirect
 #return redirect('/')


def book(request, bId):
# render the appropriate template for this request
 return None
