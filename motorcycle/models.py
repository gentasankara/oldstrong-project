from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Motorcycle(models.Model):

    year_choice = []
    for r in range(1980, (datetime.now().year+1)):
        year_choice.append((r,r))

    motorcycle_title = models.CharField(max_length=255)
    manufacture = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=255)
    miles = models.IntegerField()
    price = models.IntegerField()
    description = RichTextField()
    motor_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    motor_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    motor_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    motor_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_featured = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.motorcycle_title
