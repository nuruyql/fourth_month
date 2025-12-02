from django.contrib import admin
from .models import AboutYou

# Register your models here.
@admin.register(AboutYou)
class NewsAboutYouAdmin(admin.ModelAdmin):
    list_display = ('id',  'created_at','photo')
    search_fields = ('photo','your_name','age')
    list_filter = ('created_at',)
