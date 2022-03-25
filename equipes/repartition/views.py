from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from repartition.forms import Formulaire, UploadBookForm


def repartitionEquipes(request):
    if request.method == "POST":
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = Formulaire(request.POST)
        if form.is_valid():
            # faire des trucs
            print(form.cleaned_data["nbEquipes"])

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = Formulaire()

    return render(request, "repartition/repartitionEquipes.html", {"form": form})


def upload_file(request):
    if request.method == "POST":
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["file"])
            form.save()
    else:
        form = UploadBookForm()
    return render(request, "repartition/upload.html", {"form": form})
