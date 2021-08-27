from django.contrib import admin
from .models import User, UserPage, Page, Post
# Register your models here.
admin.site.register(User)
admin.site.register(UserPage)
admin.site.register(Page)
admin.site.register(Post)
