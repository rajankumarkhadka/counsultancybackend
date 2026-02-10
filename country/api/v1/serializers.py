from rest_framework import serializers
from country.models import Country, University, PopularCourse, StudyCost, LivingExpense, VisaRequirement, CountryOverview


class CountryOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryOverview
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class PopularCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCourse
        fields = "__all__"


class StudyCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCost
        fields = "__all__"


class LivingExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivingExpense
        fields = "__all__"


class VisaRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaRequirement
        fields = "__all__"


# Full Country Data API
class CountrySerializer(serializers.ModelSerializer):
    overview = CountryOverviewSerializer(read_only=True)
    universities = UniversitySerializer(many=True, read_only=True)
    popular_courses = PopularCourseSerializer(many=True, read_only=True)
    study_costs = StudyCostSerializer(many=True, read_only=True)
    living_expenses = LivingExpenseSerializer(many=True, read_only=True)
    visa_requirements = VisaRequirementSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = "__all__"
