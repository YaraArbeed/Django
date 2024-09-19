from django.shortcuts import render

def index(request):
# render the appropriate template for this request
 return render(request, 'bookmodule/index.html')
