from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, SigninForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'testApp/index.html')

def product(request):
    return render(request,'testApp/product.html')

def blog(request):
    return render(request,'testApp/blog.html')

def collection(request):
    return render(request,'testApp/collection.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ContactForm()

    return render(request, 'testApp/contact.html', {'form': form})

def success(request):
    return render(request, 'testApp/success.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'testApp/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = SigninForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = SigninForm()
    return render(request, 'testApp/signin.html', {'form': form})
