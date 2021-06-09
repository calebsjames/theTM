from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User


class UserView(ViewSet):
    
    # Get a single record
    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)
            
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)
    

    # # Get a list of all records
    def list(self, request):
        users = User.objects.all()
        

        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)
    

    # # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        # gamer = Gamer.objects.get(user=request.auth.user)
        user = User.objects.get(pk=pk)
        user.email = request.data["email"]
        user.first_name = request.data["first_name"]
        user.is_staff = request.data["is_staff"]
        user.is_superuser = request.data["is_superuser"]
        user.last_name = request.data["last_name"]
        user.password = request.data["password"]
        user.username = request.data["username"]
        
        user.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)
   

    # DELETE a single record 
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            user = User.objects.get(pk=pk)
            user.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'is_staff', 'is_superuser', 'last_name', 'password', 'username')
        
        