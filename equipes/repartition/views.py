from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def simple_upload(request):
    if request.method == "POST" and request.FILES["myfile"]:
        myfile = request.FILES["myfile"]
        nbEquipes = request.POST.get("nbEquipes")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(
            request,
            "repartition/simpleUpload.html",
            {"uploaded_file_url": uploaded_file_url},
        )
    return render(request, "repartition/simpleUpload.html")
