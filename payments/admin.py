from django.contrib import admin
from .models import Payments
# Register your models here.
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','motorcycle_id','motorcycle_title','price','city',
    'email','created_date','paid','payment_proof')
    list_display_links = ('id','first_name','last_name')
    search_fields = ('first_name','last_name','email','motorcycle_title')
    list_per_page = 25
admin.site.register(Payments, PaymentsAdmin)
