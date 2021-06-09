from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from tmapi.models import Show, Hotel, Promoter, Venue 



class ShowView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            show = Show.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = ShowSerializer(show, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        shows = Show.objects.all()


        serializer = ShowSerializer(
            shows, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for shows

        Returns:
            Response -- JSON serialized event instance
        """
        show = Show()
        show.advanced = request.data["advanced"]
        show.ages = request.data["ages"]
        show.artist = request.data["artist"]
        show.billing = request.data["billing"]
        show.bus_call = request.data["bus_call"]
        show.contracted = request.data["contracted"]
        show.contract_signed = request.data["contract_signed"]
        show.comments = request.data["comments"]
        show.curfew = request.data["curfew"]
        show.date = request.data["date"]
        show.date_on_calendar = request.data["date_on_calendar"]
        show.date_on_venue_site = request.data["date_on_venue_site"]
        show.date_on_artist_site = request.data["date_on_artist_site"]
        show.date_on_socials = request.data["date_on_socials"]
        show.deposit = request.data["deposit"]
        show.deposit_paid = request.data["deposit_paid"]
        show.door_price = request.data["door_price"]
        show.door_time = request.data["door_time"]
        show.drive_time = request.data["drive_time"]
        show.gross_income = request.data["gross_income"]
        show.guarantee = request.data["guarantee"]
        show.guest_list = request.data["guest_list"]
        show.guest_list_sent = request.data["guest_list_sent"]
        show.load_in = request.data["load_in"]
        show.miles_to_drive = request.data["miles_to_drive"]
        show.routing = request.data["routing"]
        show.routing_notes = request.data["routing_notes"]
        show.runner = request.data["runner"]
        show.show_length = request.data["show_length"]
        show.show_time = request.data["show_time"]
        show.sound_check = request.data["sound_check"]
        show.support = request.data["support"]
        show.status = request.data["status"]
        show.terms = request.data["terms"]
        show.ticket_sales = request.data["ticket_sales"]
        show.weather = request.data["weather"]

        hotel = Hotel.objects.get(pk=request.data["hotel"])
        show.hotel = hotel
        promoter = Promoter.objects.get(pk=request.data["promoter"])
        show.promoter = promoter
        user = User.objects.get(pk=request.data["user"])
        show.user = user
        venue = Venue.objects.get(pk=request.data["venue"])
        show.venue = venue

        try:
            show.save()
            serializer = ShowSerializer(show, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        show = Show.objects.get(pk=pk)

        show.advanced = request.data["advanced"]
        show.ages = request.data["ages"]
        show.artist = request.data["artist"]
        show.billing = request.data["billing"]
        show.bus_call = request.data["bus_call"]
        show.contracted = request.data["contracted"]
        show.contract_signed = request.data["contract_signed"]
        show.comments = request.data["comments"]
        show.curfew = request.data["curfew"]
        show.date = request.data["date"]
        show.date_on_calendar = request.data["date_on_calendar"]
        show.date_on_venue_site = request.data["date_on_venue_site"]
        show.date_on_artist_site = request.data["date_on_artist_site"]
        show.date_on_socials = request.data["date_on_socials"]
        show.deposit = request.data["deposit"]
        show.deposit_paid = request.data["deposit_paid"]
        show.door_price = request.data["door_price"]
        show.door_time = request.data["door_time"]
        show.drive_time = request.data["drive_time"]
        show.gross_income = request.data["gross_income"]
        show.guarantee = request.data["guarantee"]
        show.guest_list = request.data["guest_list"]
        show.guest_list_sent = request.data["guest_list_sent"]
        show.load_in = request.data["load_in"]
        show.miles_to_drive = request.data["miles_to_drive"]
        show.routing = request.data["routing"]
        show.routing_notes = request.data["routing_notes"]
        show.runner = request.data["runner"]
        show.show_length = request.data["show_length"]
        show.show_time = request.data["show_time"]
        show.sound_check = request.data["sound_check"]
        show.support = request.data["support"]
        show.status = request.data["status"]
        show.terms = request.data["terms"]
        show.ticket_sales = request.data["ticket_sales"]
        show.weather = request.data["weather"]

        hotel = Hotel.objects.get(pk=request.data["hotel"])
        show.hotel = hotel
        promoter = Promoter.objects.get(pk=request.data["promoter"])
        show.promoter = promoter
        user = User.objects.get(pk=request.data["user"])
        show.user = user
        venue = Venue.objects.get(pk=request.data["venue"])
        show.venue = venue

        show.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            show = Show.objects.get(pk=pk)
            show.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Show.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ShowSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Show
        fields = (
            'id', 'advanced', 'ages', 'artist', 'billing', 'bus_call', 'contracted', 'contract_signed', 
            'comments', 'curfew', 'date', 'date_on_calendar', 'date_on_venue_site', 'date_on_artist_site', 
            'date_on_socials', 'deposit', 'deposit_paid', 'door_price', 'door_time', 'drive_time', 
            'gross_income', 'guarantee', 'guest_list', 'guest_list_sent', 'hotel', 'load_in', 
            'miles_to_drive', 'promoter', 'routing', 'routing_notes', 'runner', 'show_length', 'show_time', 
            'sound_check', 'support', 'status', 'terms', 'ticket_sales', 'user', 'venue', 'weather' 
)
        depth = 1
        
