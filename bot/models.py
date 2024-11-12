from django.db import models

# Create your models here.
class  Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name 
    

class UserCredential(models.Model):
    username = models.CharField(max_length=150, unique=True)
    key = models.CharField(max_length=13)

    def __str__(self):
        return self.username