from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
path('',views.index,name='index'),
path('books',views.books),
 path('', views.index),
path('index2/<val1>/', views.index2),
path('book/<int:bId>',views.book),
path('<int:bookId>', views.viewbook)
]
