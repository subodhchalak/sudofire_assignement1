from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


# ---------------------------------------------------------------------------- #
#                              validate_mobile_no                              #
# ---------------------------------------------------------------------------- #


def validate_mobile_no(value):
    
    if value.isnumeric():
        if len(value)!=10:
            raise ValidationError("Mobile number should contain exactly 10 digits.")
        else:
            return value
    else:
        raise ValidationError("Please enter digits only.")



# ---------------------------------------------------------------------------- #
#                                 MyUser Model                                 #
# ---------------------------------------------------------------------------- #


class MyUser(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    
    mobile_no = models.CharField(
        max_length=10,
        unique=True,
        validators = [validate_mobile_no],
        null=True, blank=True,
        help_text="10 Digit Mobile Number"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created', )
        
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
    
    
# ------------------------------------ END ----------------------------------- #