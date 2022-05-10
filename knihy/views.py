from django.shortcuts import render, redirect

from .models import Kniha
from .forms import KnihaForm
# Create your views here.

def nova_kniha(request):
    if request.method == "POST":
        form = KnihaForm(request.POST)
        if form.is_valid():
            jmeno = form.cleaned_data["jmeno"]
            nova_kniha = Kniha(jmeno=jmeno)
            nova_kniha.save()
            return redirect("podekovani")
    else:
        form = KnihaForm()
    context = {"form": form}
    return render(request, "knihy/nova_kniha.html", context)


def dekuji(request):
    return render(request, "knihy/dekuji.html")

