from django.contrib import admin

from customer_app.models import Customer


# Register your models here.


# ---------------------------------------------------------------------------- #
#                                 CustomerAdmin                                #
# ---------------------------------------------------------------------------- #


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer', 'profile_no', ]
    list_display_links = ['customer', 'profile_no', ]
    list_filter = ['created', ]
    
    
    
# ------------------------------------ END ----------------------------------- #