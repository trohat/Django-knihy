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

class NovaKniha(View):
    def post(self, request):
        form = KnihaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("podekovani")
        context = {"form": form}
        return render(request, "knihy/nova_kniha.html", context)

    def get(self, request):
        form = KnihaForm()
        context = {"form": form}
        return render(request, "knihy/nova_kniha.html", context)
        
def nova_kniha(request):
    if request.method == "POST":
        form = KnihaForm(request.POST)
        if form.is_valid():
            form.save()
            #jmeno = form.cleaned_data["jmeno"]
            #autor = form.cleaned_data["autor"]
            #recenze = form.cleaned_data["recenze"]
            #nova_kniha = Kniha(jmeno=jmeno, autor=autor, recenze=recenze)
            #nova_kniha.save()
            return redirect("podekovani")
    else:
        form = KnihaForm()
    context = {"form": form}
    return render(request, "knihy/nova_kniha.html", context)

def dekuji(request):
    return render(request, "knihy/dekuji.html", {"jmeno_slona": "Dumbo"})

class Dekuji(TemplateView):
    template_name = "knihy/dekuji.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jmeno_slona"] = "Jumbo"
        return context
    
def seznam(request):
    knihy = Kniha.objects.all()
    return render(request, "knihy/seznam.html", {"knihy": knihy})

class Seznam(TemplateView):
    template_name = "knihy/seznam.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        knihy = Kniha.objects.all()
        context["knihy"] = knihy
        return context

class Seznam2(ListView):
    model = Kniha
    template_name = "knihy/seznam.html"
    context_object_name = "knihy"
    #queryset = Kniha.objects.all()[7:]

def detail(request, id):
    kniha = Kniha.objects.get(id=id)
    return render(request, "knihy/detail.html", {"kniha": kniha})

class Detail(DetailView):
    model = Kniha
    template_name = "knihy/detail.html"

# tohle teď už neplatí --- tohle jsou view funkce
# budeme z nich dělat třídy, tedy class-based views
