from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import string
import random


class MailSender:
    def send_mail(email, booking_code):
        context = {'email':email, 'booking_code':booking_code}
        message = render_to_string('creator_email_authenticate.html', context)
        email = EmailMessage(
            subject    = 'Flight Ticket Reference Code',
            body       = message,
            to         = [email],
        )
        email.content_subtype = 'html'
        email.send()
        
def generate_reference_code(length=6):
    """Generate a random PIN of the specified length."""
    characters = string.digits  
    pin = ''.join(random.choice(characters) for _ in range(length))
    return pin

