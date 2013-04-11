from django.db import models

# Create your models here.
from django.db import models

class Caption(models.Model):
    string = models.CharField(max_length=255)