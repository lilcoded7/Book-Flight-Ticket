from django.urls import path, include
from ticket.views import FlightAPIView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'book', BookFlightView, basename='book')

urlpatterns = [
    # path('', include(router.urls)),
    path('book/', FlightAPIView.as_view())
]