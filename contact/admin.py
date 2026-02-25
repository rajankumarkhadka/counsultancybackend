
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Contact,CounselingSession

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'interested_destination', 'phone_number', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'interested_destination', 'message')
    readonly_fields = ('created_at', 'updated_at',)
    exclude = ['ip_address', 'user_agent']

    def action_buttons(self, obj):
        edit_url = reverse('admin:contacts_contact_change', args=[obj.id])
        return format_html(
            '<a href="{}" style="padding:4px 10px; background-color:#28A745; color:white; '
            'border-radius:5px; text-decoration:none; margin-right:5px; font-weight:bold;">Edit</a>',
            edit_url
        )
    action_buttons.short_description = 'Actions'

admin.site.register(Contact, ContactAdmin)




@admin.register(CounselingSession)
class CounselingSessionAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'interested_country',
        'study_level',
        'counseling_mode',
        'preferred_date',
        'preferred_time',
        'status',
        'created_at',
    )

    list_filter = ('status', 'counseling_mode', 'interested_country')
    search_fields = ('full_name', 'email', 'phone')
