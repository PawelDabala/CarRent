from django.urls import path
from .views import User_view, Address_view
# from .views import

urlpatterns = [
    path('users/', User_view, name='users'),
    path('addresses/', Address_view, name='addresses'),
]
