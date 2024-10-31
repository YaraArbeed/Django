from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
path('',views.index,name='index'),
path('books',views.books),
path('books2',views.books2),
path('filterbooks',views.filterbooks),
path('book/<int:bId>',views.book),
#----------------------Lab4--------------------------------------
 path('index', views.lab_index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
#----------------------Lab5---------------------------------------
path('books/html5/links', views.html5_links, name='links'),
path('books/html5/text/formatting/', views.html5_text_formatting, name='text_formatting'),
path('books/html5/listing/', views.html5_listing, name='listing'),
path('books/html5/tables', views.html5_tables, name='tables'),
#---------------------Lab6--------------------------------------
path('books/search', views.search, name='search'),
#---------------------Lab7------------------------------------
path('books/simple/query', views.simple_query, name='query'),
path('books/complex/query', views.lookup_query, name='lookup_query'),


]
