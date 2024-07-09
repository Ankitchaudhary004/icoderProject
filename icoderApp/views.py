from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
      return render(request,'index.html')

# def about(request):
#       return render(request,'about.html')

def contact(request):
      return render(request,'contact.html')
      #return HttpResponse('this is contact page')

def tec(request):
      return render(request,'tec.html')
      #return HttpResponse('this is contact page')

def showhome(request):
    slideObj = home.objects.all()
    data=container.objects.all()
    template_name = 'index.html'
    context = {'slideObj':slideObj,'data':data}
    return render(request, template_name, context)



def showAbout(request):
    aboutObj = about.objects.all()
    template_name = 'about.html'
    context = {'aboutObj':aboutObj}
    return render(request, template_name, context)



def contact(request):
             if request.method=='POST':
               fname=request.POST['fname']
               lname=request.POST['lname']
               country=request.POST['country']
               subject=request.POST['subject']
               print(fname,lname,country,subject)
               contact=Contact(fname=fname,lname=lname,country=country,subject=subject)
               contact.save()
              #return HttpResponse("<h1>Thanks for Contact Us</h1>")
               messages.success(request, 'Form submit successfully')
             return render (request,'contact.html')
