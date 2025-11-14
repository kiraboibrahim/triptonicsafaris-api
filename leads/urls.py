from django.urls import path
from .views import SpecialOfferCreateView, NewsletterCreateView

urlpatterns = [
    path("special-offer/", SpecialOfferCreateView.as_view()),
    path("newsletter/", NewsletterCreateView.as_view()),
]
