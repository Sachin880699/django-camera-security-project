from django.shortcuts import render,redirect
from.forms import *

def home(request):

    return render(request,'home/home.html')


def add_camera(request):
    if request.method=="POST":
        form = Add_camera_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Add_camera_Forms()

    return render(request,'home/add_camera.html',{"New_Camera_Form":form})




def view_camera(request):

    data = Add_camera.objects.all()

    return render(request,'home/view_camera.html',{"data":data})





def edit(request, id):
    contactData = Add_camera.objects.get(id=id)
    return render(request,'home/edit.html', {'contactData':contactData})



'''def update(request, id):
    contactData = New_Camera.objects.get(id=id)
    form = New_Camera_Form(request.POST, instance = contactData)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'home/edit.html', {'contactData': contactData})'''



def update(request, id):
    contactData = Add_camera.objects.get(id=id)
    form = Add_camera_Forms(request.POST, instance = contactData)
    if form.is_valid():
        form.save()
        return redirect("view_camera")
    return render(request, 'home/edit.html', {'contactData': contactData})



def delete(request, id):
    contacts = Add_camera.objects.get(id=id)
    contacts.delete()
    return redirect("view_camera")



def linear(request):
    return render(request,'algorithm/linear.html')


def logistic(request):
    return render(request,'algorithm/logistic.html')

#-----------------This is company Login----------------------


def company_login(request):

    company_name = Company_register.objects.values('company_name')
    password_first = Company_register.objects.values('password_first')

    username = request.POST.get('username')
    password = request.POST.get('password')

    company_name = [d['company_name'] for d in company_name]
    password_first = [d['password_first'] for d in password_first]
    if username in company_name and password in password_first:
        print('OK')

    else:
        error = 'Username or password is wrong'
        return render(request,'home/company_login.html',{'error':error})


    return render(request,'home/company_login.html')


#-------------------------End company login----------------------


#-------------------------company Register----------------------

def company_register(request):
    if request.method=="POST":
        form = Company_register_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Company_register_Form()



    return render(request,'home/company_register.html',{"form":form})


def batch(request):
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BatchForm()

    #return render(request, 'hotel_image_form.html', {'form' : form})


    return render(request,'home/batch.html',{'form':form})


def person_entry(request):
    if request.method=='POST':
        form  = PersonEntryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PersonEntryForm()

    return render(request,'home/person_entry.html',{'form':form})





