from django.contrib import admin
from .models import *


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


admin.site.register(Event)
admin.site.register(MYClubUser)
# admin.site.register(Venue)
