from django.urls import path
from .views import User_view, Address_view, User_add
# from .views import

urlpatterns = [
    path('users/', User_view, name='users'),
    path('addresses/', Address_view, name='addresses'),
    path('users/add', User_add, name='user_add'),
]
