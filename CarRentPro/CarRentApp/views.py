from django.shortcuts import render, redirect
from .models import User, Address, Maciek
from .forms import AddressForm, MaciekForm, CarForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def User_view(request):
    users = User.objects.all()
    context = {
        'users': users
    }

    return render(request, 'users.html', context=context)


def User_add(request):
    if request.method == "GET":
        return render(request, 'user_add.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        User.objects.create(name=name, last_name=last_name, password=password)
        return HttpResponseRedirect(reverse('users'))


def Address_view(request):
    addresses = Address.objects.all()
    print(addresses)
    context = {
        'addresses': addresses
    }
    return render(request, 'addresses.html', context)


def AddressSingle_view(request):
    context = {
        "form": AddressForm
    }

    return render(request, 'address.html', context)


def AddressAdd_views(request):
    myform = AddressForm(request.POST)
    print(myform)

    # if myform.is_valid():
    myaddress = Address(street=myform.cleaned_data['street'],
                        bulding=myform.cleaned_data['bulding'],
                        flat=myform.cleaned_data['flat'],
                        post_code=myform.cleaned_data['post_code'],
                        city=myform.cleaned_data['city'])
    myaddress.save()

    return redirect('addresses')


def Maciek_view(request):
    context = {
        "form": MaciekForm
    }

    return render(request, 'maciek.html', context)


def MaciekAdd_view(request):
    form = MaciekForm(request.POST)

    if form.is_valid():
        mymaciek = Maciek(name=form.cleaned_data['name'])

        mymaciek.save()

    return redirect('maciek')

def Car_view(request):
    context = {
        'carform': CarForm
    }
    return render(request, 'car_add.html', context)

def CarAdd_view(request):
    mycarform = CarForm(request.POST)

    if mycarform.is_valid():
        mycarform.save()

    return redirect('car')




