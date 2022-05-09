from django.db import models

# Create your models here.

class Kniha(models.Model):
    jmeno = models.CharField(max_length=200)

    def __str__(self):
        return self.jmeno