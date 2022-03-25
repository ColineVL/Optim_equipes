from django import forms


class Formulaire(forms.Form):
    nbEquipes = forms.CharField()
