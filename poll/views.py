from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from .forms import Registration
from .models import student_register

# Create your views here.
def register(request):
    if request.method=='POST':
        fm=Registration(request.POST)
        if fm.is_valid():
            fname=fm.cleaned_data['fname'] 
            lname=fm.cleaned_data['lname'] 
            mail=fm.cleaned_data['email']
            pwd1=fm.cleaned_data['password1']
            pwd2=fm.cleaned_data['password1']
            gen=fm.cleaned_data['gender']
            col=fm.cleaned_data['color'] 

            data=student_register(fname=fname,lname=lname,email=mail,password1=pwd1,password2=pwd2,gender=gen,color=col)
            data.save()
           

            print("First name:\t",fname)
            print("Last name:\t",lname)
            print("Email address:\t",mail)
            print("password:\t",pwd1)
            print("password:\t",pwd2)
            print("Gender:\t",gen)
            print("chose color:\t",col)
            # return redirect("/")
            # return HttpResponseRedirect("/")
            # fm=Registration()
            # return HttpResponse('Form submited successfully!!')
            return HttpResponseRedirect('thanksww/')
    else:
        fm=Registration()

    return render(request,'home.html',{'form':fm})

def thank(request):
    return render(request,'thank.html')
