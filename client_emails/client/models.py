
from django.db import models

class Client(models.Model):
       name = models.CharField(max_length=100)
       email = models.EmailField()

       def str(self):
           return self.name