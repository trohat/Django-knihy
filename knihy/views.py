from django.shortcuts import render, redirect

from .models import Kniha
from .forms import KnihaForm
# Create your views here.

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
    return render(request, "knihy/dekuji.html")

