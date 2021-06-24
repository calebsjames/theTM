from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tmapi.models import Venue



class VenueView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            venue = Venue.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = VenueSerializer(venue, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        venues = Venue.objects.all()


        serializer = VenueSerializer(
            venues, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for venues

        Returns:
            Response -- JSON serialized event instance
        """
        venue = Venue()
        venue.address = request.data["address"]
        venue.capacity = request.data["capacity"]
        venue.cell = request.data["cell"]
        venue.city = request.data["city"]
        venue.email = request.data["email"]
        venue.hall_fee = request.data["hall_fee"]
        venue.merch_sales = request.data["merch_sales"]
        venue.merch_fee = request.data["merch_fee"]
        venue.name = request.data["name"]
        venue.phone = request.data["phone"]
        venue.state = request.data["state"]
        venue.website = request.data["website"]
        venue.zip = request.data["zip"]

        try:
            venue.save()
            serializer = VenueSerializer(venue, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        venue = Venue.objects.get(pk=pk)

        venue.address = request.data["address"]
        venue.capacity = request.data["capacity"]
        venue.contact = request.data["contact"]
        venue.cell = request.data["cell"]
        venue.city = request.data["city"]
        venue.email = request.data["email"]
        venue.hall_fee = request.data["hall_fee"]
        venue.merch_sales = request.data["merch_sales"]
        venue.merch_fee = request.data["merch_fee"]
        venue.name = request.data["name"]
        venue.phone = request.data["phone"]
        venue.state = request.data["state"]
        venue.website = request.data["website"]
        venue.zip = request.data["zip"]

        venue.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            venue = Venue.objects.get(pk=pk)
            venue.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Venue.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class VenueSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Venue
        fields = (
            'id', 'address', 'capacity', 'cell', 'city', 'email', 'hall_fee', 'merch_sales',
             'merch_fee', 'name', 'phone', 'state', 'website', 'zip')
        
