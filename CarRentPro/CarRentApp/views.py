from django.shortcuts import render
from .models import User, Address

# Create your views here.
def User_view(request):
    users = User.objects.all()
    context = {
        'users': users
    }

    return render(request, 'users.html', context=context)

def Address_view(request):
    addresses = Address.objects.all()
    print(addresses)
    context = {
        'addresses': addresses
    }
    return render(request, 'addresses.html', context)