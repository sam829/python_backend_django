from django.db import models


# Create your models here.
class Notes(models.Model):
    text = models.TextField()


class Customer(models.Model):
    name = models.CharField("name", max_length=255)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
