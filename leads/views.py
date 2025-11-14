from rest_framework import generics
from .models import SpecialOfferLead, NewsletterSubscriber
from .serializers import SpecialOfferSerializer, NewsletterSerializer

class SpecialOfferCreateView(generics.CreateAPIView):
    queryset = SpecialOfferLead.objects.all()
    serializer_class = SpecialOfferSerializer

class NewsletterCreateView(generics.CreateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSerializer
