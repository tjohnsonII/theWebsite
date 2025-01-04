from django.urls import path
from . import views
from .views import signup
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),  # Map root URL to `home` view
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
