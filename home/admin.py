from django.contrib import admin
from .models import StudyAbroadCard, SuccessStoryCard, SocialMedia, ContactInfo

# ================================
# STUDY ABROAD CARD
# ================================
@admin.register(StudyAbroadCard)
class StudyAbroadCardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'image')
        }),
        ('Icons (JSON)', {
            'fields': ('icons',),
            'classes': ('collapse',),
            'description': 'Add icons as JSON array, e.g. [{"name":"Visa","icon":"/media/icons/visa.png"}]'
        }),
    )
    def display_name(self, obj):
        return obj.title  # You can replace obj.title with any custom name
    display_name.short_description = "Study Abroad "

# ================================
# SUCCESS STORY CARD
# ================================
@admin.register(SuccessStoryCard)
class SuccessStoryCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'education', 'university')
    search_fields = ('name', 'education', 'university')
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'education', 'university', 'description')
        }),
    )


# ================================
# SOCIAL MEDIA
# ================================
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'link')
    search_fields = ('platform_name',)
    fieldsets = (
        ('Social Media Info', {
            'fields': ('platform_name', 'icon', 'link')
        }),
    )


# ================================
# CONTACT INFO
# ================================
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('location', 'phone')
    search_fields = ('location', 'phone', 'address')
    fieldsets = (
        ('Contact Details', {
            'fields': ('location', 'phone', 'address')
        }),
        ('Social Media Links (JSON)', {
            'fields': ('social_media',),
            'classes': ('collapse',),
            'description': 'Add social media links as JSON array, e.g. [{"platform":"Facebook","icon":"/media/icons/fb.png","link":"https://fb.com"}]'
        }),
    )
