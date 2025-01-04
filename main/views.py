
# Create your views here.
from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from blog.models import BlogPost

def home(request):
    context = {
        'title': 'Welcome',
        'message': 'This is a dynamic message!',
    }
    posts = BlogPost.objects.all()
    return render(request, 'main/home.html', {'posts': posts})
    #return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Example: Sending an email (configure email backend in settings.py)
        send_mail(
            f"Contact Form Submission from {name}",
            message,
            email,
            ['your_email@example.com']
        )

        return redirect('/')  # Redirect to home or a success page

    return render(request, 'contact.html')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the actual name of your login URL
        else:
            print(form.errors)  # Debugging: Print form errors to the console
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/signup.html', {'form': form})



def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        BlogPost.objects.create(title=title, content=content)
        return redirect('/blog/blog_home/')
    return render(request, 'create_post.html')
