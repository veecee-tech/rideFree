from django.urls import path
from .views import *


urlpatterns = [
    path('home/', booker_home, name='booker-home'),
    path('place-order/', place_order_view, name='place'),
    path('manage/', myOrders, name='manage-orders'),
    path('manage/order/<str:booking_id>', order_detail, name='order_detail'),
    path('manage/order/cancel/<str:booking_id>', cancel_order, name='cancel_order'),
    path('profile/', booker_profile_view, name='update-profile'),
]



