from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Kniha
from .forms import KnihaForm
# Create your views here.

class NovaKniha2(LoginRequiredMixin, FormView):
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
    posledni = request.session.get("posledni", "žádná")
    return render(request, "knihy/seznam.html", {"knihy": knihy, "posledni": posledni})

@login_required
def detail(request, pk):
    kniha = Kniha.objects.get(pk=pk)
    request.session["posledni"] = kniha.jmeno
    return render(request, "knihy/detail.html", {"kniha": kniha})


# tohle teď už neplatí --- tohle jsou view funkce
# budeme z nich dělat třídy, tedy class-based views
