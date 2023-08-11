from django.db.models.signals import post_save
from ticket.models.flight import Flight
from ticket.models.booking import Booking
from ticket.utils import generate_reference_code
from django.dispatch import receiver
from .utils import MailSender


@receiver(post_save, sender=Flight)
def send_reference_code(sender, instance, created, **kwargs):
    if created:
        booking = Booking.objects.create(
            passenger_name=instance.passenger_name,
            flight=instance,
            booking_reference=generate_reference_code()
        )
        booking.booking_reference = generate_reference_code()
        MailSender.send_mail(instance.passenger_email, generate_reference_code)
    