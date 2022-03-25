from django.shortcuts import render
from django.conf import settings
import os

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


def download_file(request):
    # fill these variables with real values
    filename = "effectifs.xlsx"
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(
                fh.read(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = "attachment; filename=%s" % filename
            return response
