from django.db import models

# Create your models here.

class Email(models.Model):
    pixel_id = models.CharField(max_length=254)
    subject = models.CharField(max_length=500)
    date = models.DateField()
    user_to = models.EmailField(max_length=254)
    user_cc = models.EmailField(max_length=254, null=True)
    seen = models.IntegerField(default=0)


