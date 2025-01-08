from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost, Profile

# Register the BlogPost model
#admin.site.register(BlogPost)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number')