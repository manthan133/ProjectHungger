from django.shortcuts import render, redirect
from django.http import HttpResponse, response, Http404
from .models import food,user,cart

from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required #will be used in cart
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import logout
from django.db import connection
from django.template import loader

from django.contrib.sessions.models import Session

import pdfkit

# Create your views here.
# https://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/

def findfood(request):
    type = 'Available'

    if request.method == 'GET' and 'type' in request.GET:
        type = request.GET['type']

    if type != 'Available':
        result = food.objects.filter(type=type)
    else:
        result = food.objects.all()

    type = type.title()

    context = {'result': result, 'type': type}
    return render(request, 'food.html', context)

def goto(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'AboutUs.html')

def placeorder(request):
    request.session['total_amt']=0
    username = request.session.get('username')
    order = cart.objects.filter(user_id=username)
    total = 0
    for item in order:
        total = total+(item.qty*item.food_id.price)
    request.session['total_amt']=total
    #request.session['final_amt']=total
    cart.objects.filter(user_id=username).delete()
    request.session['cart_count']=get_cart_count(username)
    return render(request,'PlaceOrder.html')

@csrf_protect
def home(request):

    context={}

    types = food.objects.values('type').distinct()

    if request.method == 'POST' and 'name' in request.POST:
        context=signup(request)
    elif request.method == 'POST' and 'email' in request.POST and 'password' in request.POST:
        context=login(request)
    elif request.method == 'POST' and 'logout' in request.POST:
        if request.session.session_key:
            request.session.flush()

    context.update({'types':types})

    return render(request, 'index.html', context)

def signup(request):
    email=request.POST['email']
    name=request.POST['name']
    address=request.POST['address']
    password=request.POST['password']

    isExist = user.objects.filter(email=email).count()

    if isExist == 0:
        newuser = user(email=email,name=name,password=password,address=address)
        newuser.save()
        signedup=True
        context = {'signedup': signedup}
    else:
        exist = True
        context = {'exist':exist}
    return context


def login(request):
    email = request.POST['email']
    passwd = request.POST['password']
    if user.objects.filter(email=email).exists() and user.objects.get(email=email).password == passwd:
        request.session['username'] = email
        request.session['name'] = user.objects.get(email=email).name.title()
        request.session['address'] = user.objects.get(email=email).address
        request.session['cart_count'] = get_cart_count(email)
        request.session.save()
        context = {}
    else:
        invalid = True
        context = {'invalid': invalid}
    return context

def get_cart_count(username):
    return cart.objects.filter(user_id=username).count()

@csrf_protect
def addToCart(request):

    if request.method == 'POST' and 'food_id' in request.POST:
        username=request.session.get('username')
        food_id=request.POST['food_id']

        cart_food = cart.objects.filter(user_id=username).filter(food_id=food_id)

        if(cart_food.count() == 0):
            cart_user = user.objects.get(email=username)
            cartfood = food.objects.get(food_id=food_id)
            add = cart(user_id=cart_user,food_id=cartfood,qty=1)
            add.save()
        else:
            for item in cart_food:
                count=item.qty
            cart_food.update(qty=count+1)
        request.session['cart_count']=get_cart_count(username)
        items = cart.objects.filter(user_id=request.session.get('username'))
        context = {'items': items}
    else:
        if request.session.session_key:
            items=cart.objects.filter(user_id=request.session.get('username'))
            context={'items':items}
        else:
            raise Http404("Login First to View Cart")


    return render(request, 'cart.html', context)
