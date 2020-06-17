from django.shortcuts import render,redirect,HttpResponseRedirect
from . models import Student
from .forms import StudentRegister

# Create your views here.
def index(request):
    student = Student.objects.all()
    if request.method == 'POST':
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            fn=fm.cleaned_data['firstname']
            ln=fm.cleaned_data['lastname']
            em=fm.cleaned_data['email']
            reg = Student(firstname=fn,lastname=ln,email=em)
            reg.save()
            return redirect('index')

    else:
        fm = StudentRegister()
        student = Student.objects.all()

    return render(request,'student/index.html',{'form':fm,'stud':student})



def editData(request,id):
    if request.method == 'POST':
        pi=Student.objects.get(pk=id)
        fm=StudentRegister(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            # return HttpResponseRedirect('/')
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegister(instance=pi)

    return render(request,'student/update.html',{'form':fm})

def deleteData(request,id):
    if request.method == 'POST':
        u_id = Student.objects.get(pk=id)
        u_id.delete()
        return HttpResponseRedirect('/')