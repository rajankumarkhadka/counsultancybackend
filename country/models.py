from django.db import models
from filehub.fields import ImagePickerField
from tinymce.models import HTMLField


# ================================
# MAIN COUNTRY MODEL
# ================================
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    total_students = models.PositiveIntegerField()
    subtitle = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True, blank=False, max_length=255)
    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Country"           # Singular name
        verbose_name_plural = "Countries"  # Plural name


# ================================
# COUNTRY OVERVIEW
# ================================
class CountryOverview(models.Model):
    country = models.OneToOneField(
        Country,
        on_delete=models.CASCADE,
        related_name="overview"
    )
    title = models.CharField(max_length=200)
    description = HTMLField()
    key_highlights = HTMLField(help_text="Comma separated or bullet points")
    image = ImagePickerField(upload_to="country_overviews/ ", blank=True)
    def __str__(self):
        return f"{self.country.country_name} Overview"

    class Meta:
        verbose_name = "Country Overview"
        verbose_name_plural = "Country Overviews"

# ================================
# UNIVERSITIES
# ================================
class University(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="universities"
    )
    name = models.CharField(max_length=255)
    world_rank = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    avg_tuition_cost = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
# ================================
# POPULAR COURSES
# ================================
class PopularCourse(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="popular_courses"
    )
    name = models.CharField(max_length=200)
    avg_annual_fee = models.CharField(max_length=100, blank=True)  # Can be a range or average

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Popular Course"
        verbose_name_plural = "Popular Courses"
# ================================
# STUDY COST (By Level)
# ================================
class StudyCost(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="study_costs"
    )
    study_level = models.CharField(max_length=100)   # Bachelor, Master, PhD
    avg_annual_fee = models.CharField(max_length=100, blank=True)  # Can be a range or average

    def __str__(self):
        return f"{self.study_level} - {self.country.country_name}"

    class Meta:
        verbose_name = "Study Cost"
        verbose_name_plural = "Study Costs"


# ================================
# LIVING EXPENSES
# ================================
class LivingExpense(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="living_expenses"
    )
    type = models.CharField(max_length=200)  
    price = models.CharField(max_length=100,blank=True)  # Can be a range or average
    icon = models.CharField(max_length=100, blank=True, help_text="Huge Icon class name")

    def __str__(self):
        return f"{self.type} - {self.country.country_name}"

    class Meta:
        verbose_name = "Living Expense"
        verbose_name_plural = "Living Expenses"

# ================================
# VISA REQUIREMENTS
# ================================
class VisaRequirement(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="visa_requirements"
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    icon = models.CharField(max_length=100, blank=True, help_text="Huge Icon class name")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Visa Requirement"
        verbose_name_plural = "Visa Requirements"

class KeyHighlight(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="key_highlights"
    )
    city = models.CharField(max_length=200)
    city_description = models.CharField(max_length=200)
    currency = models.CharField(max_length=100, blank=True)
    currency_description = models.CharField(max_length=200, blank=True)
    intake_months = models.CharField(max_length=100, blank=True)

   

    def __str__(self):
        return self.city
    class Meta:
        verbose_name = "Key Highlight"
        verbose_name_plural = "Key Highlights"