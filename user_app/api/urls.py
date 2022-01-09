from django.urls import path

from user_app.api.views import myuser_list, myuser_detail

urlpatterns = [
    path('myuser_list/', myuser_list, name='myuser-list'),
    path('myuser_list/<int:pk>/detail/', myuser_detail, name='myuser-detail'),
]