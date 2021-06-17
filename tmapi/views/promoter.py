from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tmapi.models import Promoter



class PromoterView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            promoter = Promoter.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = PromoterSerializer(promoter, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        promoters = Promoter.objects.all()


        serializer = PromoterSerializer(
            promoters, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for promoters

        Returns:
            Response -- JSON serialized event instance
        """
        promoter = Promoter()
        promoter.address = request.data["address"]
        promoter.cell_phone = request.data["cell_phone"]
        promoter.city = request.data["city"]
        promoter.comments = request.data["comments"]
        promoter.company = request.data["company"]
        promoter.email = request.data["email"]
        promoter.name = request.data["name"]
        promoter.phone = request.data["phone"]
        promoter.state = request.data["state"]
        promoter.zip = request.data["zip"]

        try:
            promoter.save()
            serializer = PromoterSerializer(promoter, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        promoter = Promoter.objects.get(pk=pk)

        promoter.address = request.data["address"]
        promoter.cell_phone = request.data["cell_phone"]
        promoter.city = request.data["city"]
        promoter.comments = request.data["comments"]
        promoter.company = request.data["company"]
        promoter.email = request.data["email"]
        promoter.name = request.data["name"]
        promoter.phone = request.data["phone"]
        promoter.state = request.data["state"]
        promoter.zip = request.data["zip"]

        promoter.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            promoter = Promoter.objects.get(pk=pk)
            promoter.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Promoter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class PromoterSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Promoter
        fields = ('id', 'address', 'cell_phone', 'city', 'comments', 'company', 'email', 'name', 'phone', 'state', 'zip')
        
