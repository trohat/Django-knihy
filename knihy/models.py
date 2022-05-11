from django.db import models

# Create your models here.

class Kniha(models.Model):
    jmeno = models.CharField(max_length=20)
    autor = models.CharField(max_length=200)
    recenze = models.TextField()

    class Meta:
        verbose_name_plural = "Knihy"

    def __str__(self):
        return self.jmeno