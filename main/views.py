
# Create your views here.
from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import CustomUserCreationForm
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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

        # Send email
        email_message = EmailMessage(
            subject=f"Contact Form Submission from {name}",
            body=message,
            from_email='tim2@timsablab.ddns.net',  # Must match EMAIL_HOST_USER
            to=['tim2@timsablab.ddns.net'],  # Replace with the recipient email
            reply_to=[email],  # User's input email
        )
        email_message.send(fail_silently=False)

        return redirect('/')  # Redirect to home or a success page

    return render(request, template_name='contact.html')

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


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                user.profile  # Check if the user has a profile
            except User.profile.RelatedObjectDoesNotExist:
                # Redirect to sign-up if no profile exists
                messages.error(request, "No profile found for this account. Please sign up.")
                return redirect('signup')

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'main/login.html')

def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_home.html', {'posts': posts})