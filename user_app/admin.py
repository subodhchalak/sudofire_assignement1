from django.contrib import admin

from user_app.models import MyUser
from customer_app.models import Customer

# Register your models here.


class CustomerInline(admin.TabularInline):
    model = Customer
    extra = 0


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'mobile_no']
    list_filter = ['first_name', 'last_name']
    inlines = [CustomerInline, ]