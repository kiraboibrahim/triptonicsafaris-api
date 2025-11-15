from django.contrib import admin

from .models import BookingRequest


class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('destination', 'depart_date', 'return_date', 'duration', 'created_at')
    search_fields = ('destination',)
    list_filter = ('destination', 'created_at')


admin.site.register(BookingRequest, BookingRequestAdmin)