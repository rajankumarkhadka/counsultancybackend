from django.contrib import admin
from django.utils.html import format_html
from .models import StudyAbroadCard, SuccessStoryCard, SocialMedia, ContactInfo,TeamMember, SocialMediaLink,Core_value, About

# ================================
# STUDY ABROAD CARD
# ================================
@admin.register(StudyAbroadCard)
class StudyAbroadCardAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'button_text', 'url', 'image_tag')
    search_fields = ('title',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'image')
        }),
        ('Additional Info', {
            'fields': ('icons', 'button_text', 'url'),
            'classes': ('collapse',),
        }),
    )
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%; object-fit:cover;" />', obj.image)
        return "-"
    image_tag.short_description = 'Image'
    
    def display_name(self, obj):
        return obj.title  # You can replace obj.title with any custom name
    display_name.short_description = "Study Abroad "

# ================================
# SUCCESS STORY CARD
# ================================
@admin.register(SuccessStoryCard)
class SuccessStoryCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'education', 'university', 'image_tag')
    search_fields = ('name', 'education', 'university')
    fieldsets = (
        ('Basic Info', {
            'fields': ('name','image', 'education', 'university', 'description')
        }),
    )
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%; object-fit:cover;" />', obj.image)
        return "-"
    image_tag.short_description = 'Image'

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
    list_display = ( 'phone', 'email', 'address',)
    search_fields = ('location', 'phone', 'address')
    fieldsets = (
        ('Contact Details', {
            'fields': ('location', 'phone', 'address', 'business_hour', 'email')
        }),
    )



class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1  # number of empty link rows

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    inlines = [SocialMediaLinkInline]
    list_display = ('name', 'position','description', 'image_tag')
    search_fields = ('name', 'position')
    fieldsets = (
        ('Team Member Info', {
            'fields': ('name', 'position', 'description', 'image')
        }),
    )
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%; object-fit:cover;" />', obj.image)
        return "-"
    image_tag.short_description = 'Image'   

    


@admin.register(Core_value)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'description')
    search_fields = ('title', 'description')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_preview')
    search_fields = ('title',)

    def description_preview(self, obj):
        return obj.description[:100] + "..." if len(obj.description) > 100 else obj.description
    description_preview.short_description = "Description Preview"