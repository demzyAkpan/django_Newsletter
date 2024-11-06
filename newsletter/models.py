from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Newletter(models.Model):
    title = models.CharField(max_length=50, blank=False)
    body = models.CharField(max_length=200, blank=False)