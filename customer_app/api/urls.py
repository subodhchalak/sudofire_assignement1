from django.urls import path

from customer_app.api.views import customer_list, customer_detail


urlpatterns = [
    path('customer_list/', customer_list, name='customer-list'),
    path('customer_list/<int:pk>/detail/', customer_detail, name='customer-detail'),
]