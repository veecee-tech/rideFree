from django.shortcuts import render, redirect
from django.contrib import messages
from orders.models import Orders
# Create your views here.


def dashboard(request):
    recent_orders_placed = Orders.objects.filter(payed=True, order_status="pending")
    accepted = Orders.objects.filter(rider = request.user, order_status="received")
    completed = Orders.objects.filter(rider=request.user, order_status='completed')

    context = {
        'recent_orders_placed': recent_orders_placed.count(),
        'accepted': accepted.count(),
        'completed': completed.count(),
        
    }

    
    return render(request, 'rider/home.html', context)

def recent_orders(request):
    recent_orders_placed = Orders.objects.filter(payed=True, order_status="pending")

    context = {
        'orders': recent_orders_placed
    }
    return render(request, 'rider/recent_orders.html', context)

def accept_order(request, id):
    order = Orders.objects.get(id=id)
    order.order_status = 'received'
    order.rider = request.user
    order.save()
    return redirect('accepted_order')

def accepted_order(request):

    if request.method == "POST":

        booking_id = request.POST.get('booking_id')

        try:

            order = Orders.objects.get(booking_id = booking_id, rider = request.user)
        except Orders.DoesNotExist:
            messages.error(request, "Invalid ID")
            return redirect('accepted_order')

        if order:
            order.order_status = "completed"
            order.save()
            messages.success(request, "Order Completed Successfully")


        return redirect('accepted_order')
        
    
    try:
        accepted_order = Orders.objects.get(rider = request.user, order_status="received")
    except Orders.DoesNotExist:
        accepted_order = None

    context = {
        'order': accepted_order
    }
    return render(request, 'rider/accepted.html', context)
