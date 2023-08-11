from rest_framework import serializers
from ticket.models.flight import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['passenger_name', 'passenger_email', 'departure_city', 'arrival_city', 'departure_date']

    