from django import forms


"""
class KnihaForm(forms.Form):
    jmeno = forms.CharField(max_length=200, 
                label="Zadej jméno knihy",
                error_messages={
                    "required": "Tohle políčko je povinné",
                    "max_length": "Moc dlouhý text, povoleno je maximálně 20 znaků."
                })
    autor = forms.CharField(max_length=100, label="Jméno autora")
    recenze = forms.CharField(max_length=2000, 
        label="Recenze knihy",
        widget=forms.Textarea)
"""


from .models import Kniha


class KnihaForm(forms.ModelForm):
    class Meta:
        model = Kniha
        fields = "__all__"  #pozor toto je mírně nebezpečné
        labels = {
            "jmeno": "Zadej jméno knihy:",
            "autor": "Zadej jméno autora:",
            "recenze": "Napiš něco o knize"
        }
        error_messages = {
            "jmeno": {
                    "required": "Tohle políčko je povinné",
                    "max_length": "Toto je moc dlouhý text, povoleno je maximálně 20 znaků."
                }
        }


