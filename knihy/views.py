from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView

from .models import Kniha
from .forms import KnihaForm
# Create your views here.

class NovaKniha2(FormView):
    form_class = KnihaForm
    template_name = "knihy/nova_kniha.html"
    success_url = "dekuji"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def dekuji(request):
    return render(request, "knihy/dekuji.html")
    
def seznam(request):
    knihy = Kniha.objects.all()
    return render(request, "knihy/seznam.html", {"knihy": knihy})

def detail(request, id):
    kniha = Kniha.objects.get(id=id)
    return render(request, "knihy/detail.html", {"kniha": kniha})


# tohle teď už neplatí --- tohle jsou view funkce
# budeme z nich dělat třídy, tedy class-based views
