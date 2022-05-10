from django import forms

class KnihaForm(forms.Form):
    jmeno = forms.CharField(max_length=20, 
                label="Zadej jméno knihy")


