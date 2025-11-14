from django.db import models
from destinations.constants import DESTINATION_CHOICES

class BookingRequest(models.Model):
    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES)
    depart_date = models.DateField()
    return_date = models.DateField()
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.destination} on {self.depart_date}"
