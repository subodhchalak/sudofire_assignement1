from django.db.models.signals import post_save, post_delete
from user_app.models import MyUser
from customer_app.models import Customer



# ---------------------------------------------------------------------------- #
#                            customer_created Signal                           #
# ---------------------------------------------------------------------------- #


def customer_created(sender, instance, created, **kwargs):
    
    if created:
        myuser = instance
        customer_create = Customer.objects.create(
            customer=myuser,
        )
        

# ---------------------------------------------------------------------------- #
#                       calling customer_created function                      #
# ---------------------------------------------------------------------------- #

# Everytime new 'MyUser' is generated, its 'profile_no' will automatically gnerated

post_save.connect(customer_created, sender=MyUser)


# ------------------------------------ END ----------------------------------- #