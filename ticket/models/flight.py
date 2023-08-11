from django.db import models


class Flight(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def update_flight(request, email):
        flight = Flight.objects.get(passenger_name=passenger_name)
        flight.passenger_email=email
        flight.save()

   
    def __str__(self):
        return f'{self.passenger_name} {self.flight_number} {self.departure_city}'