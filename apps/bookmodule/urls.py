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
 path('list_books/', views.list_books2, name= "books.list_books"),
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
#----------------------AI project--------------------------------------
path('predict', views.predict, name='predict'),
path('home', views.home, name='home'),
#----------------------Lab8----------------------------------------------
path('books/lab8/task1', views.lab8_task1, name='lab8_task1'),
path('books/lab8/task2', views.lab8_task2, name='lab8_task2'),
path('books/lab8/task3', views.lab8_task3, name='lab8_task3'),
path('books/lab8/task4', views.lab8_task4, name='lab8_task4'),
path('books/lab8/task5', views.lab8_task5, name='lab8_task5'),
path('books/lab8/task7', views.lab8_task7, name='lab8_task7'),
#------------------------Revision-----------------------------
path('books/revision/task1', views.revision_task1, name='revision_task1'),  # Landing Page
path('books/revision/task2', views.revision_task2, name='revision_task2'),  # List Books Page
path('books/revision/task3/<int:book_id>/', views.revision_task3, name='revision_task3'), # Book Details Page
#------------------------Lab9-----------------------------------------------
    path('books/lab9_part1/listbooks', views.list_books, name='list_books'),
    path('books/lab9_part1/addbook', views.add_book, name='add_book'),
    path('books/lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('books/lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    path('books/lab9_part2/listbooks', views.list_books_form, name='list_books_form'),
    path('books/lab9_part2/addbook', views.add_book_form, name='add_book_form'),
    path('books/lab9_part2/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
    path('books/lab9_part2/deletebook/<int:id>', views.delete_book_form, name='delete_book_form'),
#--------------------------Lab10--------------------------------------------------
    path('students/', views.list_students, name='list_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('students2/', views.list_students2, name='list_students2'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('students2/edit/<int:pk>/', views.edit_student2, name='edit_student2'),
    path('students2/delete/<int:pk>/', views.delete_student2, name='delete_student2'),
    path('images/upload/', views.upload_image, name='upload_image'),
    path('images/', views.list_images, name='list_images'),
    #-------------------------Lecture9---------------------
    path('addBook',views.addBook,name='addBook'),
    path('updateBook/<int:bId>',views.updateBook,name='updateBook'),
    path('listBooks',views.listBooks,name='listBooks'),
    path('readBook/<int:bId>',views.readBook,name='readBook'),
    path('deleteBook/<int:bId>', views.deleteBook, name="deleteBook"),
    #--------------------------Lecture10--------------------------------
    path('addBook3',views.addBook3,name='addBook3'),

    
    
]
