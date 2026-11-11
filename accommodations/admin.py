from django.contrib import admin
from .models import Photo, Hotel

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Hotel, HotelAdmin)