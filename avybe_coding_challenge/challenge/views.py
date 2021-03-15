from django.shortcuts import get_object_or_404, render,HttpResponseRedirect
from .models import Information
from .forms import InformationForm
from django.http import HttpResponse 
from .import forms

def upload_to_home(request): 
    context ={}
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = InformationForm() 
    context['form']= InformationForm()
    return render(request, "challenge/upload_to_home.html", context) 

#def home(request):
 #   return render(request, 'challenge/home.html',{'title':'Home'})

def home(request): 
  
    if request.method == 'GET': 
        data = Information.objects.last()  
        return render(request, 'challenge/home.html', 
                     {'info' : data})

