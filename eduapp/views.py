from django.shortcuts import render
from .models import student

# Create your views here.
def index(request):
    stude1 = student.objects.all()
    

    
    return render(request,'index.html',{'stude1' : stude1})