from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Payments
from django.core.mail import send_mail
from django.contrib.auth.models import User




# Create your views here.
def order(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        motorcycle_id = request.POST['motorcycle_id']
        motorcycle_title = request.POST['motorcycle_title']
        price = request.POST['price']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        payment_proof = request.FILES['payment_proof']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_order = Payments.objects.all().filter(motorcycle_id=motorcycle_id, user_id=user_id)
            if has_order:
                messages.error(request, 'You have already make an order for this Motorcycle.')
                return redirect('/motorcycle/'+motorcycle_id)

        payments = Payments(first_name=first_name, last_name=last_name,motorcycle_id=motorcycle_id,
                    motorcycle_title=motorcycle_title,price=price,city=city,state=state,email=email,phone=phone,
                    user_id=user_id,payment_proof=payment_proof)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New Motorcycle Order',
                'You Have a new order for the motorcycle '+motorcycle_title+'. Please login to admin panel to confirm the payment',
                'oldrstrongweb@gmail.com',
                [admin_email],
                fail_silently=False,
            )

        payments.save()
        messages.success(request, 'Thaknyou for your order, we will confim your payment as soon as possible.')
        return redirect('/motorcycle/'+motorcycle_id)
