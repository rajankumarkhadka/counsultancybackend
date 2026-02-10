from django.contrib import admin
from .models import *

# ================================
# INLINE TABLES (Tabular for multiple items)
# ================================
class TestCardInline(admin.StackedInline):
    model = TestCard
    extra = 1


class WhyChooseInline(admin.StackedInline):
    model = WhyChoose
    extra = 1


class TestFormatInline(admin.StackedInline):
    model = TestFormat
    extra = 1


class CourseCurriculumInline(admin.StackedInline):
    model = CourseCurriculum
    extra = 1
    ordering = ('week',)


# ================================
# SINGLE STACKED INLINE (one per test)
# ================================
class TestOverviewInline(admin.StackedInline):
    model = TestOverview
    max_num = 1
    can_delete = False
    verbose_name_plural = "Overview"


class CoursePricingInline(admin.StackedInline):
    model = CoursePricing
    max_num = 1
    can_delete = False
    verbose_name_plural = "Pricing"


# ================================
# TEST PREPARATION ADMIN
# ================================
@admin.register(TestPreparation)
class TestPreparationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

    inlines = [
        TestOverviewInline,      # Stacked inline
        TestCardInline,          # Tabular inline
        WhyChooseInline,         # Tabular inline
        TestFormatInline,        # Tabular inline
        CourseCurriculumInline,  # Tabular inline
        CoursePricingInline      # Stacked inline
    ]
