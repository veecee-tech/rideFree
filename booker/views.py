from django.shortcuts import render, redirect
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

# @login_required 
# def booker_profile_view(request):
    
#     forms = BookerProfileForm(instance=request.user.adviserprofile)
    
#     if request.method == "POST":
#         forms = BookProfileForm(request.POST, request.FILES or None, instance=request.user.bookerprofile)

#         if forms.is_valid():
#             forms.save()
#             messages.success(request, "Edit adviser Info Successfully!")
#             return redirect("update-adviser")

#     context = {
#         "forms": forms,
#     }
#     return render(request, "booker/profile.html", context)

# @login_required()

def myOrders(request):
    orders = Orders.objects.filter(booker=request.user)

    if orders:
        context = {
            'orders': orders
        }

    return render(request, 'booker/manage-orders.html', context)

@login_required
def order_detail(request, booking_id):

    try:
        order = Orders.objects.get(booking_id=booking_id)

        context = {
            'order': order
        }
        return render(request, 'booker/order-details.html', context)
    except Exception as e:

        pass
@login_required
def cancel_order(request, booking_id):

    order = Orders.objects.get(booking_id=booking_id)

    order.order_status = 'cancelled'
    order.save()
    return redirect('manage-orders')

@login_required
def fund_wallet(request):
    return render(request, 'booker/fund.html')