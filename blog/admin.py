from django.contrib import admin
from django.utils.html import format_html
from .models import BlogType, Blog
from tinymce.widgets import TinyMCE
from django import forms

# --- Blog form for TinyMCE ---
class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = Blog
        fields = '__all__'

# --- Blog Admin ---
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'blog_type', 'published_date', 'image_display', 'slug')
    list_filter = ('blog_type', 'published_date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

    def image_display(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="40" style="object-fit: cover; border-radius: 4px;" />',
                obj.image
            )
        return "-"
    image_display.short_description = 'Image'

# --- BlogType Admin ---
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
