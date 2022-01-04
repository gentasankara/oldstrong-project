from django.shortcuts import render, redirect
from motorcycle.models import Motorcycle
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    featured_motor = Motorcycle.objects.order_by('-created_date').filter(is_featured=True)
    all_motor = Motorcycle.objects.order_by('-created_date')
    #search_fields = Motorcycle.objects.values('manufacture','model','year')
    manufacture_search = Motorcycle.objects.values_list('manufacture', flat=True).distinct()
    model_search = Motorcycle.objects.values_list('model', flat=True).distinct()
    year_search = Motorcycle.objects.values_list('year', flat=True).distinct()
    data ={
        'featured_motor' : featured_motor,
        'all_motor' : all_motor,
        #'search_fields' : search_fields,
        'manufacture_search' : manufacture_search,
        'model_search' : model_search,
        'year_search' : year_search,
    }

    return render(request, 'pages/home.html',data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from OldStrong Website regarding '+subject
        message_body = 'Name : ' +name+ '. \nEmail : '+email+ '. \nPhone Number : '+phone+ '. \nMessage : '+message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
                subject,
                message_body,
                'oldrstrongweb@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thankyou for concating us, we will get back to you immmidietly!')
        return redirect('contact')

    return render(request, 'pages/contact.html')
