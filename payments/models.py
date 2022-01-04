from django.db import models
from datetime import datetime

# Create your models here.
class Payments(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    motorcycle_id = models.IntegerField()
    motorcycle_title = models.CharField(max_length=100)
    price = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    payment_proof = models.FileField(upload_to ='media')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.email
