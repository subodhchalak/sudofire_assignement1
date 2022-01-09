from django.db import models

from user_app.models import MyUser

import uuid

# Create your models here.


# ---------------------------------------------------------------------------- #
#                                Customer Model                                #
# ---------------------------------------------------------------------------- #


class Customer(models.Model):
    
    customer = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="customer_profile_no")
    
    profile_no = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return str(self.profile_no)
    
    
# ------------------------------------- END ------------------------------------ #