from django.contrib import admin
from .models import *


# ================================
# INLINE TABLES
# ================================
class UniversityInline(admin.StackedInline):
    model = University
    extra = 1


class PopularCourseInline(admin.StackedInline):
    model = PopularCourse
    extra = 1


class StudyCostInline(admin.StackedInline):
    model = StudyCost
    extra = 1


class LivingExpenseInline(admin.StackedInline):
    model = LivingExpense
    extra = 1


class VisaRequirementInline(admin.StackedInline):
    model = VisaRequirement
    extra = 1


class CountryOverviewInline(admin.StackedInline):
    model = CountryOverview
    max_num = 1

class KeyHighlightInline(admin.StackedInline):
    model = KeyHighlight
    max_num = 1

# ================================
# COUNTRY ADMIN (TABBED)
# ================================
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_name", "total_students", "subtitle")
    search_fields = ("country_name",)

    inlines = [
        CountryOverviewInline,
        UniversityInline,
        PopularCourseInline,
        StudyCostInline,
        LivingExpenseInline,
        VisaRequirementInline,
        KeyHighlightInline
    ]


@admin.register(PopularCourse)
class PopularCourseAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country__country_name")

@admin.register(StudyCost)
class StudyCostAdmin(admin.ModelAdmin):
    list_display = ("country", "study_level", "avg_annual_fee")
    search_fields = ("country__country_name",)

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country__country_name")

@admin.register(LivingExpense)
class LivingExpenseAdmin(admin.ModelAdmin):
    list_display = ("country", "type", "price")
    search_fields = ("country__country_name",)

@admin.register(VisaRequirement)
class VisaRequirementAdmin(admin.ModelAdmin):
    list_display = ("country", "title")
    search_fields = ("country__country_name", "title")

@admin.register(KeyHighlight)
class KeyHighlightAdmin(admin.ModelAdmin):
    list_display = ('country', "currency", "currency_description", "intake_months")
    search_fields = ("city","country", "currrency")

   