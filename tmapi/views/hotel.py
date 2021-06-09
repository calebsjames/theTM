from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tmapi.models import Hotel



class HotelView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            hotel = Hotel.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = HotelSerializer(hotel, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        hotels = Hotel.objects.all()


        serializer = HotelSerializer(
            hotels, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for hotels

        Returns:
            Response -- JSON serialized event instance
        """
        hotel = Hotel()
        hotel.address = request.data["address"]
        hotel.confirmation = request.data["confirmation"]
        hotel.name = request.data["name"]
        hotel.notes = request.data["notes"]
        hotel.phone = request.data["phone"]


        try:
            hotel.save()
            serializer = HotelSerializer(hotel, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        hotel = Hotel.objects.get(pk=pk)

        hotel.address = request.data["address"]
        hotel.confirmation = request.data["confirmation"]
        hotel.name = request.data["name"]
        hotel.notes = request.data["notes"]
        hotel.phone = request.data["phone"]

        hotel.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            hotel = Hotel.objects.get(pk=pk)
            hotel.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Hotel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class HotelSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Hotel
        fields = (
            'id', 'address', 'confirmation', 'name', 'notes', 'phone')
        
