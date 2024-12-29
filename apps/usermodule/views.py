from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            obj = form.save()
            # should we say something here: comes next using messages
            return redirect('login')
    form = SignUpForm()
    return render(request, "usermodule/register.html", {"form": form})

def logoutUser(request):
    logout(request)
    return redirect('/')  # to landing page

from .forms import LoginForm  # Import your custom LoginForm

def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  # Use the custom LoginForm
        if form.is_valid():
            # Extract data from the form
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, "Login successful!")
                return redirect('home')  # Redirect to home or dashboard after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission or reCAPTCHA failed.")
    else:
        form = LoginForm()  # Instantiate the custom LoginForm

    return render(request, 'usermodule/login.html', {'form': form})
