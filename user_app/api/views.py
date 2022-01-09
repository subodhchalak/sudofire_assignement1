from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from user_app.api.serializers import MyUserSerializer
from user_app.models import MyUser


# ---------------------------------------------------------------------------- #
#                               myuser_list View                               #
# ---------------------------------------------------------------------------- #


@api_view(['GET', 'POST'])
def myuser_list(request):
    
    if request.method == 'GET':
        myusers = MyUser.objects.all()
        serializer = MyUserSerializer(myusers, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MyUserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

# ---------------------------------------------------------------------------- #
#                              myuser_detail View                              #
# ---------------------------------------------------------------------------- #
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def myuser_detail(request, pk):
    
    try:
       myuser = MyUser.objects.get(pk=pk)
    except MyUser.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = MyUserSerializer(myuser, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MyUserSerializer(myuser, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        myuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
# ------------------------------------ END ----------------------------------- #