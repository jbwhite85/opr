from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street = models.TextField(help_text = "IE: 203 56th Street")
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    email = models.TextField()
    phone = models.TextField(help_text = "IE: 555-555-5555")
