
from django.forms import ModelForm
from .models import Category, Colleges, Locations


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CollegeForm(ModelForm):
    class Meta:
        model = Colleges
        fields = "__all__"

class LocationForm(ModelForm):
    class Meta:
        model = Locations
        fields= "__all__"