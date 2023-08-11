from django.db import models
from ticket.models.flight import Flight
from setup.basemodel import TimeBaseModel
from django.contrib.auth.models import User


class Booking(TimeBaseModel):
    passenger_name = models.CharField(max_length=100)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_reference = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f'Reference Code:{self.booking_reference}'


        