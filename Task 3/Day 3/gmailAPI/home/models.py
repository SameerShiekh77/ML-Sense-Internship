from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, default='')
    pswd = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.name
