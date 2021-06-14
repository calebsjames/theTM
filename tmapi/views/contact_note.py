from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tmapi.models import ContactNote, Show



class ContactNoteView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            contact_note = ContactNote.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = ContactNoteSerializer(contact_note, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        contact_notes = ContactNote.objects.all()


        serializer = ContactNoteSerializer(
            contact_notes, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for contact_notes

        Returns:
            Response -- JSON serialized event instance
        """
        contact_note = ContactNote()
        contact_note.date = request.data["date"]
        contact_note.method = request.data["method"]
        contact_note.text = request.data["text"]

        show = Show.objects.get(pk=request.data['show'])
        contact_note.show = show

        try:
            contact_note.save()
            serializer = ContactNoteSerializer(contact_note, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        contact_note = ContactNote.objects.get(pk=pk)

        contact_note.date = request.data["date"]
        contact_note.method = request.data["method"]
        contact_note.text = request.data["text"]

        show = Show.objects.get(pk=request.data["show"])
        contact_note.show = show

        contact_note.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            contact_note = ContactNote.objects.get(pk=pk)
            contact_note.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ContactNote.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ContactNoteSerializer(serializers.ModelSerializer):   
    class Meta:
        model = ContactNote
        fields = (
            'id', 'date', 'method', 'text', 'show')
        depth = 1
        
