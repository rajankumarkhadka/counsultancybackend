from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import Blog

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            "description": TinyMCE(attrs={"cols": 80, "rows": 10}),
        }

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

    list_display = (
        "title",
        "category",
        "published_date",
        "slug",
        "short_description",
    )

    search_fields = ("title", "category", "description")

    list_filter = ("published_date", "category")


    prepopulated_fields = {"slug": ("title",)}

    def short_description(self, obj):
        return obj.description[:50] + "..." if obj.description else ""
    short_description.short_description = "Description"

    ordering = ("-published_date",)

    save_on_top = True

    fieldsets = (
        ("Basic Info", {"fields": ("category", "title", "slug", "published_date")}),
        ("Content", {"fields": ("description", "image")}),
    )
