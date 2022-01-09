from rest_framework import serializers

from user_app.models import MyUser
from customer_app.api.serializers import CustomerSerializer


# ---------------------------------------------------------------------------- #
#                               MyUserSerializer                               #
# ---------------------------------------------------------------------------- #


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    
    # Nested serialization
    customer_profile_no = CustomerSerializer(many=False, read_only=True)
    
    class Meta:
        model = MyUser
        fields = '__all__'
        
        
# ------------------------------------- X ------------------------------------ #