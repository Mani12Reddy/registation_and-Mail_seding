from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
from django.core.mail import send_mail
def home(request):
    return render(request,'home.html')

def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        print(2)
        if UD.is_valid() and PD.is_valid():
            print(3)
            US=UD.save(commit=False)
            pw=UD.cleaned_data['password']
            US.set_password(pw)
            US.save()

            PS=PD.save(commit=False)
            PS.user=US
            PS.save()


            send_mail('User registration',
            'Regiistration is success full',
            'manikantareddy6385@gmail.com',
            [US.email],fail_silently=False)



            return HttpResponse('registered')
    return render(request,'registration.html',d)