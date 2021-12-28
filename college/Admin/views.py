from django.shortcuts import render

from django.shortcuts import render, redirect
from .form import CategoryForm, CollegeForm
from .models import Category, Colleges
from django.contrib import messages
from .filters import LocationFilter
from django.contrib.auth.decorators import login_required


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/show_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add category')
            return render(request, 'Admin/add_category.html', {'add_category':form})
    context ={
        'form_category': CategoryForm,
        'activate_category': 'active'
    }
    return render(request, 'Admin/add_category.html', context)


def dashboard(request):
    return render(request,'Admin/dashboard.html')


def show_category(request):
    categories = Category.objects.all().order_by('-id')
    context={
        'categories':categories,
        'activate_category':'active'
    }
    return render(request,'Admin/show_category.html',context)


def update_category(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/show_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add category')
            return render(request, 'Admin/add_category.html', {'add_category':form})
    context ={
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active'
    }
    return render(request, 'Admin/add_category.html', context)


def delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'Category deleted successfully')
    return redirect('/show_category')

# list of college


def add_college(request):
    if request.method == "POST":
        form = CollegeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'College added successfully')
            return redirect("/show_colleges")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add college')
            return render(request, 'Admin/add_category.html', {'add_college':form})
    context ={
        'form_category': CollegeForm,
        'activate_category': 'active'
    }
    return render(request, 'Admin/add_college.html', context)


def show_college(request):
    colleges = Colleges.objects.all().order_by('-id')
    # location_filter = LocationFilter(request.GET, queryset=colleges)
    # location_final = location_filter.qs
    context={
        'colleges':colleges,
        # 'location_filter': location_filter,
        'activate_college':'active'
    }
    return render(request,'Admin/show_colleges.html',context)


def update_college(request,college_id):
    college = Colleges.objects.get(id=college_id)
    if request.method == "POST":
        form = CollegeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'College added successfully')
            return redirect("/show_colleges")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add college')
            return render(request, 'Admin/add_college.html', {'add_college':form})
    context ={
        'form_category': CollegeForm(instance=college),
        'activate_category': 'active'
    }
    return render(request, 'Admin/add_college.html', context)


def delete_college(request,college_id):
    college= Colleges.objects.get(id=college_id)
    college.delete()
    messages.add_message(request,messages.SUCCESS,'College deleted successfully')
    return redirect('/show_colleges')

# show location and colleges


def show_location_college(request):
    colleges = Colleges.objects.all().order_by('-id')
    location_filter = LocationFilter(request.GET, queryset=colleges)
    location_final = location_filter.qs
    context = {
        'colleges': location_final,
        'location_filter': location_filter,
        'activate_college': 'active'
    }
    return render(request,'Admin/show_location_college.html',context)
