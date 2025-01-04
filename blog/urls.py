
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('blog_home/', views.blog_home, name='blog_home'),  # Explicit blog_home path
    path('<int:post_id>/', views.blog_post, name='blog_post'),
    path('', views.blog_home, name='blog_home'),  # Blog homepage

]
