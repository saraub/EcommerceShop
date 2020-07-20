from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse
import json
import datetime
from  .decorators import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,CustomerForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='store_main')
def store(request):
    if request.user.is_authenticated:       
        customer= request.user.customer
        order, created= Order.objects.get_or_create(customer=customer)
        items= order.ordereditem_set.all()
        cartitems=order.get_total_num_cart
    else:
        items=['']
        order=[]
        cartitems=[]
    
    items=Item.objects.all()
    context= {'items':items,'order':order,'cartitems':cartitems}


    return render(request, 'store/store.html', context)

@login_required(login_url='login')
def cart(request):

    if request.user.is_authenticated:       
        customer= request.user.customer
        order, created= Order.objects.get_or_create(customer=customer)
        items= order.ordereditem_set.all()
        cartitems=order.get_total_num_cart
    else:
        items=['']
        order=[]
        cartitems=[]
    context={'items':items,'order':order,'cartitems':cartitems}


    return render(request,'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:       
        customer= request.user.customer
        order, created= Order.objects.get_or_create(customer=customer)
        items= order.ordereditem_set.all()
        cartitems=order.get_total_num_cart
    else:
        items=['']
        order=[]
        cartitems=[]
    context={'items':items,'order':order,'cartitems':cartitems}
    return render(request,'store/checkout.html', context)

def update(request):
    data= json.loads(request.body)
    itemid= data['itemid']
    action= data['action']
    
    print('itemid:',itemid)
    print('action:',action)
    
    customer=request.user.customer
    item= Item.objects.get(id=itemid)
    order, created= Order.objects.get_or_create(customer=customer)
    orderitem, created= OrderedItem.objects.get_or_create(order=order, item=item)
    
    
    if action=='add':
        orderitem.quantity=(orderitem.quantity +1)
    elif action=='remove':
        orderitem.quantity=(orderitem.quantity -1)
        
    orderitem.save()
    
    if orderitem.quantity <=0:
        orderitem.delete()
        
    return JsonResponse('item was added',safe=False)

def payment(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
	

	total = float(data['form']['total'])
	order.trans_id = transaction_id

	if total == order.get_total_price_cart:
		
	    order.save()

	ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)
		

	return JsonResponse('Payment submitted..', safe=False)
@unauthenticated_user
def registerPage(request):
 
        
    
        form= CreateUserForm()
        
        
        if request.method == 'POST':
            form= CreateUserForm(request.POST)
            
            if form.is_valid():
                user= form.save()
                username= form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                
                Customer.objects.create(
                    user=user,
                    name=username
                    
				)
                messages.success(request,'Account has been created for'+ username)
                return redirect('login')
                
        
        context={'form': form}
        return render(request, 'store/register.html',context)
    
@unauthenticated_user
def loginPage(request):
    
    if request.method=='POST':
       username= request.POST.get('username')
       password= request.POST.get('password')
       
       
           
       user=authenticate(request, username=username,password= password)
       if user is not None:
            login(request, user)
            return redirect('store')
       else:
           messages.info(request, 'Username or Password is incorrect')
           
    
    context = {}
    return render(request, 'store/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def detail(request,id):
    
    item=Item.objects.get(id=id)
    customer= request.user.customer
    order, created= Order.objects.get_or_create(customer=customer)
    cartitems=order.get_total_num_cart
    context={'item':item,'cartitems':cartitems,'order':order}
    return render(request,'store/detail.html',context)

def store_main(request):
    items= Item.objects.all()
    context ={'items':items}
    return render(request,'store/store_main.html',context)