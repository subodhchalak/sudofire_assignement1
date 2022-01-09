from rest_framework import serializers

from customer_app.models import Customer



# ---------------------------------------------------------------------------- #
#                              CustomerSerializer                              #
# ---------------------------------------------------------------------------- #


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ('profile_no', 'created',)


# ------------------------------------- X ------------------------------------ #