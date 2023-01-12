from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.dashboard, name="rider-home"),
    path('orders/', views.recent_orders, name="recent_orders"),
    path('accepted/', views.accepted_order, name="accepted_order"),
    path('accept/<int:id>/', views.accept_order, name="accept_order"),
    path('pending/', views.pending_orders, name='pending_orders'),
    path('completed/', views.completed_orders, name='completed_orders'),
]
