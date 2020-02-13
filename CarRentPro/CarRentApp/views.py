from django.shortcuts import render
from .models import User, Address
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
