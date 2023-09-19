from django.contrib import admin

# Register your models here.

from .models import Bloguser,Blog,Blogdetails,Resume,Student,Mark,Person,PersonAddress,City,Interest
# Register your models here.

admin.site.register(Bloguser)

admin.site.register(Blog)
admin.site.register(Blogdetails)

admin.site.register(Resume)

admin.site.register(Student)

admin.site.register(Mark)

admin.site.register([Person,PersonAddress,City,Interest])