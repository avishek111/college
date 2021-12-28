import django_filters
from .models import Colleges
from .form import CollegeForm
from django.contrib.auth.models import User, Group
from django_filters import CharFilter


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Colleges
        fields = "__all__"
        exclude= ['college_level','college_type','college_popularity','college_annual_cost','college_image']
