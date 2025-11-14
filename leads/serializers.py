from rest_framework import serializers
from .models import SpecialOfferLead, NewsletterSubscriber

class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOfferLead
        fields = "__all__"

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = "__all__"
