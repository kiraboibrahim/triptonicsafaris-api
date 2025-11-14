from rest_framework import generics
from .models import BookingRequest
from .serializers import BookingRequestSerializer

class BookingRequestCreateView(generics.CreateAPIView):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
