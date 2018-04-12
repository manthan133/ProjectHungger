from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name='index'),
    url('^AboutUs',views.about,name='about'),
    url('^food',views.findfood,name='food'),
    url('^cart',views.addToCart,name='cart'),
    url('^PlaceOrder',views.placeorder,name='placeorder'),
]
