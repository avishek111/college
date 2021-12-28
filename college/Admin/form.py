
from django.forms import ModelForm
from .models import Category, Colleges


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CollegeForm(ModelForm):
    class Meta:
        model = Colleges
        fields = "__all__"