from django.db import models
from destinations.constants import DESTINATION_CHOICES

class SpecialOfferLead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.destination}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
