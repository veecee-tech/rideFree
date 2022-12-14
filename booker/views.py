from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orders.models import Orders, SourceDestination
from .forms import *
from django_currentuser.middleware import get_current_authenticated_user
from django.contrib.auth.decorators import login_required
from orders.models import Orders
# Create your views here.


@login_required
def booker_home(request):

    all_orders = Orders.objects.filter(booker=request.user)

    context = {
        'all': all_orders.count(),
        'completed': all_orders.filter(order_status = 'completed').count(),
        'cancelled': all_orders.filter(order_status = 'cancelled').count(),
        'pending': all_orders.filter(order_status = 'pending').count()
    }

    return render(request, 'booker/home.html', context)

@login_required
def place_order_view(request):  
    forms = OrderForm(request.POST or None)
    if request.method == "POST"  or None:
        forms = OrderForm(request.POST or None)    
        if forms.is_valid():
            forms.save()           
            return redirect("manage-orders")
    context = {
        "forms": forms,
    }
    return render(request, "booker/place-order.html", context)

@login_required 
def booker_profile_view(request):
    
    forms = BookerProfileForm(instance=request.user.bookerprofile)
    
    if request.method == "POST":
        forms = BookerProfileForm(request.POST, instance=request.user.bookerprofile)

        if forms.is_valid():
            forms.save()
            messages.success(request, "Edit profile Info Successfully!")
            return redirect("update-profile")

    context = {
        "forms": forms,
    }
    return render(request, "booker/profile.html", context)

@login_required
def myOrders(request):
    try:
        orders = Orders.objects.filter(booker=request.user)
    except Exception as e:
        raise e
    

   
    context = {
        'orders': orders
    }

    return render(request, 'booker/manage-orders.html', context)

@login_required
def order_detail(request, booking_id):
    
    try:
        order = get_object_or_404(Orders,booking_id=booking_id)

    except Exception as e:
        raise e
    context = {
            'order': order
        }
    return render(request, 'booker/order-details.html', context)

@login_required
def cancel_order(request, booking_id):
    try:
        order = get_object_or_404(Orders,booking_id=booking_id)
    except Exception as e:
        raise e
    order.order_status = 'cancelled'
    order.save()
    return redirect('manage-orders')
