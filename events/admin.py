from django.contrib import admin
from .models import Event
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_seats')  # Display the name and max_seats fields in the admin list view
    list_editable = ('max_seats',) 