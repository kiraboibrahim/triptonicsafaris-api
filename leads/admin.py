from django.contrib import admin

from .models import SpecialOfferLead, NewsletterSubscriber

class SpecialOfferLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'destination', 'created_at')
    search_fields = ('name', 'email', 'destination')
    list_filter = ('destination', 'created_at')

class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    list_filter = ('created_at',)


admin.site.register(SpecialOfferLead, SpecialOfferLeadAdmin)
admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)