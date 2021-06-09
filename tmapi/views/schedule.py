from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tmapi.models import Schedule, Show



class ScheduleView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            schedule = Schedule.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = ScheduleSerializer(schedule, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        schedules = Schedule.objects.all()


        serializer = ScheduleSerializer(
            schedules, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for schedules

        Returns:
            Response -- JSON serialized event instance
        """
        schedule = Schedule()
        schedule.date = request.data["date"]
        schedule.description = request.data["description"]
        schedule.time = request.data["time"]

        show = Show.objects.get(pk=request.data["show"])
        schedule.show = show

        try:
            schedule.save()
            serializer = ScheduleSerializer(schedule, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        schedule = Schedule.objects.get(pk=pk)

        schedule.date = request.data["date"]
        schedule.description = request.data["description"]
        schedule.time = request.data["time"]

        show = Show.objects.get(pk=request.data["show"])
        schedule.show = show

        schedule.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            schedule = Schedule.objects.get(pk=pk)
            schedule.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Schedule.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ScheduleSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Schedule
        fields = (
            'id', 'date', 'description', 'time', 'show')
        depth = 1
        
