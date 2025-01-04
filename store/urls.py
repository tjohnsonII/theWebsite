
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='store_home'),
    path('store_home/', views.store_home, name='store_home'),  # Explicit store_home path
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('', views.store_home, name='store_home'),  # Store homepage

]
