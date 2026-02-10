from django.db import models


# ================================
# MAIN COUNTRY MODEL
# ================================
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    total_students = models.PositiveIntegerField()
    subtitle = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.country_name


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
    description = models.TextField()
    key_highlights = models.TextField(help_text="Comma separated or bullet points")

    def __str__(self):
        return f"{self.country.country_name} Overview"


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
    avg_tuition_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


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
    avg_annual_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


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
    avg_annual_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.study_level} - {self.country.country_name}"


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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    icon = models.ImageField(upload_to="living_expense_icons/")

    def __str__(self):
        return f"{self.type} - {self.country.country_name}"


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
    icon = models.ImageField(upload_to="visa_icons/")

    def __str__(self):
        return self.title
