from django.shortcuts import render

# Create your views here.
def mdb_download(request):
    return render(request,'mdb_download.html')
