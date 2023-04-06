from django.shortcuts import render

# Create your views here
from app.models import *
def topic_display(request):
    l=Topic.objects.all()
    d={'topic':l}
    return render(request,'topic_display.html',d)

def webpage_display(request):
    l=Webpage.objects.all()
    d={'webpage':l}
    return render(request,'webpage_display.html',d)

def records_display(request):
    l1=AccessRecords.objects.all()
    d={'access':l1}
    return render(request,'records_display.html',d)