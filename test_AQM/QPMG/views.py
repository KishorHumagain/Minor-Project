from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
import os
from django.contrib import messages
from django.http import Http404, HttpResponse
from .models import FilesAdmin, Question


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Wrong credential!!!Ask admin for updating your details')
            return redirect('/')

        
    else:   
        return render(request, 'login.html' )






def logout(request):
    auth.logout(request)
    return redirect('/')


def dashboard(request):
    context = {
        'file': FilesAdmin.objects.all(),
        'user' : User.objects.all()
    }
    return render(request,'dashboard.html',context)

def download( request ,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists():
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['content-Disposition']='inline;filename='+ os.path.basename(file_path)
            return response
    
    raise Http404


def fullmark_validation(request):
    full_mark = request.POST['full_mark']
    two_mark = request.POST['two_mark']
    four_mark = request.POST['four_mark']
    full_mark = int(full_mark)
    two_mark = int(two_mark)
    four_mark = int(four_mark)
    total_two = 2*two_mark
    total_four = 4* four_mark
    if(full_mark==(total_two+total_four)):
        return render(request,'download.html')
    else:
        return redirect('dashboard')

def downloadfromhere(request):
    context={
        'file' : FilesAdmin.objects.all()
    }
    return render(request,'download.html',context)

def uploadtoadm(pdf_path):
    if FilesAdmin.objects.filter(adminupload = pdf_path).exists():
        new_file = FilesAdmin.objects.create(adminupload= pdf_path)
        new_file.save()



x = uploadtoadm('dbms_lab.pdf')



