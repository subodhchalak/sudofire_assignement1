from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from customer_app.models import Customer
from customer_app.api.serializers import CustomerSerializer


# Create your views here.

# ---------------------------------------------------------------------------- #
#                              customer_list View                              #
# ---------------------------------------------------------------------------- #


@api_view(['GET', 'POST', ])
def customer_list(request):
    
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# ---------------------------------------------------------------------------- #
#                             customer_detail View                             #
# ---------------------------------------------------------------------------- #
    

@api_view(['GET', 'DELETE'])
def customer_detail(request, pk):
    
    try:
        customer_instance = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer_instance)
        return Response(serializer.data)

    
    elif request.method == 'DELETE':
        customer_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
# ------------------------------------ END ----------------------------------- #