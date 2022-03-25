from django import forms

from repartition.models import EBooksModel


class Formulaire(forms.Form):
    nbEquipes = forms.CharField()


class UploadBookForm(forms.ModelForm):
    class Meta:
        model = EBooksModel
        fields = (
            "title",
            "pdf",
        )
