from django.contrib import admin
from .models import Motorcycle
from django.utils.html import format_html
# Register your models here.

class MotorAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.motor_photo.url))

    thumbnail.short_description='Motorcycle Image'
    list_display = ('id','thumbnail','motorcycle_title','manufacture','model','condition','price','is_featured','sold')
    list_display_links = ('id','thumbnail','motorcycle_title')
    list_editable = ('is_featured',)
    search_fields = ('id','motorcycle_title','manufacture','model','condition')
    list_filter = ('manufacture','condition','price')
admin.site.register(Motorcycle,MotorAdmin)
