from django.shortcuts import render, redirect

from .models import Kniha
# Create your views here.

def nova_kniha(request):
    if request.method == "POST":
        print("Formulář byl odeslán....")
        jmeno_nove_knihy = request.POST["jmeno"]
        if jmeno_nove_knihy != "":
            nova_kniha = Kniha(jmeno=jmeno_nove_knihy)
            nova_kniha.save()
            return redirect("podekovani")
    return render(request, "knihy/nova_kniha.html")

def dekuji(request):
    return render(request, "knihy/dekuji.html")

