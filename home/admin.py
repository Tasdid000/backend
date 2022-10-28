from django.contrib import admin
from .models import *
# Register your models here.
class Contactadmin(admin.ModelAdmin):
    list_display= ['name', 'email', "Phone"]

class Meta:
   model = Contact

admin.site.register(Contact, Contactadmin)

class orderadmin(admin.ModelAdmin):
    list_display= ['name', 'email', "Phone"]

class Meta:
   model = order

admin.site.register(order, orderadmin)

class JobApplyadmin(admin.ModelAdmin):
    list_display= ['fname', 'email', "Phone"]

class Meta:
   model = JobApply

admin.site.register(JobApply, JobApplyadmin)

@admin.register(Portfolio)
class Portfolioadmin(admin.ModelAdmin):
    class Media: 
        js = ('tiny.js',)

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)

@admin.register(Job)
class Jobadmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)



@admin.register(certifications)
class certificationsadmin(admin.ModelAdmin):
    class Media:
        js = ()