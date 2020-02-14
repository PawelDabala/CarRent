from django.urls import path
from .views import User_view, Address_view, User_add, AddressSingle_view, AddressAdd_views, Maciek_view, MaciekAdd_view
# from .views import

urlpatterns = [
    path('users/', User_view, name='users'),
    path('addresses/', Address_view, name='addresses'),
    path('users/add', User_add, name='user_add'),
    path('address', AddressSingle_view, name='address'),
    path('address_add', AddressAdd_views, name='address_add'),
    path('maciek', Maciek_view, name='maciek'),
    path('maciekadd', MaciekAdd_view, name='maciekadd')
]
