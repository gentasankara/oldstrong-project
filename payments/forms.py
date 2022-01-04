from django import forms
from .models import Payments

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = ('first_name','last_name','motorcycle_id','motorcycle_title','price'
        ,'city','state','email','phone','user_id','created_date','payment_proof')
