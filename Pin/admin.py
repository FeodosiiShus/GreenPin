from django.contrib import admin

from .models import Pin, Category, StatusPin, Images, Crowdfunding

# Register your models here.
admin.site.register(Pin)
admin.site.register(Category)
admin.site.register(StatusPin)
admin.site.register(Images)
admin.site.register(Crowdfunding)
