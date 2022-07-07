from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.TextField()
    quote_author = models.CharField(max_length=60)
