from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, generics
from .serializers import FlightSerializer
from rest_framework.permissions import IsAuthenticated
from ticket.models.booking import Booking
from ticket.models.flight import Flight


class FlightAPIView(generics.GenericAPIView):
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'flight ticket has been booked'}, 201)
        return Response({'messages':'Booking Failed!'}, status=404)


