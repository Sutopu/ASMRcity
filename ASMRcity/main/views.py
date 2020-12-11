from django.shortcuts import render
from django.http import HttpResponse
from .models import AsmrVideo
def home(request):
    videos = AsmrVideo.objects.all()
    return render(request, "main/home.html", {"videos":videos})
# Create your views here.
