from django.contrib import admin
from .models import *


# ================================
# INLINE TABLES
# ================================
class UniversityInline(admin.TabularInline):
    model = University
    extra = 1


class PopularCourseInline(admin.TabularInline):
    model = PopularCourse
    extra = 1


class StudyCostInline(admin.TabularInline):
    model = StudyCost
    extra = 1


class LivingExpenseInline(admin.TabularInline):
    model = LivingExpense
    extra = 1


class VisaRequirementInline(admin.TabularInline):
    model = VisaRequirement
    extra = 1


class CountryOverviewInline(admin.StackedInline):
    model = CountryOverview
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
        VisaRequirementInline
    ]
