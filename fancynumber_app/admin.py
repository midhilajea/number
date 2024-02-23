from django.contrib import admin
from .models import FancyPhoneNumber

class FancyPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'amount')  # Display these fields in the list view
    search_fields = ('number',)  # Enable search by number
    list_filter = ('amount',)  # Enable filtering by amount
    ordering = ('number',)  # Sort by number by default
    # You can add more configurations as needed

# Register the model with the custom admin options
admin.site.register(FancyPhoneNumber, FancyPhoneNumberAdmin)
