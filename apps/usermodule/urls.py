from django.urls import path
from .views import loginUser, registerUser, logoutUser

urlpatterns = [
    path('login/', loginUser, name="login"),
    path('register/', registerUser, name="register"),
    path("logout/", logoutUser, name="logout"),

]