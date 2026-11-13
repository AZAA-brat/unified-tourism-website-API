from django.contrib import admin
from .models import Photo, Hotel, Phone, City

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 4

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, PhoneInline]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(City)