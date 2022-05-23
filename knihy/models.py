from django.db import models
from django.urls import reverse

# Create your models here.

class Kniha(models.Model):
    jmeno = models.CharField(max_length=20)
    autor = models.CharField(max_length=200)
    recenze = models.TextField()
    release = models.DateField()

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Knihy"

    def __str__(self):
        return self.jmeno