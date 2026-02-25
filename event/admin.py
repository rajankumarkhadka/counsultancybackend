from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from django.utils.html import format_html
import nested_admin

from .models import  Event, EventAgenda, EventLearning, EventUniversity

# ---------------------------
# Forms for TinyMCE
# ---------------------------
class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = Event
        fields = '__all__'

class EventAgendaInlineForm(forms.ModelForm):
    class Meta:
        model = EventAgenda
        fields = '__all__'
        widgets = {'agenda_item': TinyMCE(attrs={'cols': 80, 'rows': 10})}

class EventLearningInlineForm(forms.ModelForm):
    class Meta:
        model = EventLearning
        fields = '__all__'
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 10})}

class EventUniversityInlineForm(forms.ModelForm):
    class Meta:
        model = EventUniversity
        fields = '__all__'
        widgets = {'universities': TinyMCE(attrs={'cols': 80, 'rows': 10})}

# ---------------------------
# Nested Inlines
# ---------------------------
class EventAgendaInline(admin.StackedInline):
    model = EventAgenda
    form = EventAgendaInlineForm
    extra = 1

class EventLearningInline(admin.StackedInline):
    model = EventLearning
    form = EventLearningInlineForm
    extra = 1

class EventUniversityInline(admin.StackedInline):
    model = EventUniversity
    form = EventUniversityInlineForm
    extra = 1

class EventInline(admin.StackedInline):
    model = Event
    form = EventAdminForm
    extra = 1
    inlines = [EventAgendaInline, EventLearningInline, EventUniversityInline]
    readonly_fields = ('image_preview',)
    fields = ('title', 'description', 'date', 'time', 'location', 'icon', 'image', 'slug', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="150" height="100" style="object-fit: cover; border-radius: 6px;" />',
                obj.image
            )
        return "-"
    image_preview.short_description = 'Preview'

# ---------------------------
# Event Admin (standalone)
# ---------------------------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('title','slug','category','show_learnings', 'show_agendas', 'show_universities', 'date', 'time', 'location', 'image_display')
    list_filter = ('category', 'date')
    search_fields = ('title','category', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [EventAgendaInline, EventLearningInline, EventUniversityInline]

    def show_agendas(self, obj):
        return ", ".join([a.agenda_item[:30] for a in obj.agendas.all()])
    show_agendas.short_description = "Agendas"

    def show_learnings(self, obj):
        return ", ".join([l.content[:30] for l in obj.learnings.all()])
    show_learnings.short_description = "Learnings"

    def show_universities(self, obj):
        return ", ".join([u.universities[:30] for u in obj.universities.all()])
    show_universities.short_description = "Universities"
    def image_display(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="40" style="object-fit: cover; border-radius: 4px;" />',
                obj.image
            )
        return format_html('<span style="color: #888;">No Image</span>')
    image_display.short_description = 'Image'

