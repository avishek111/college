from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('',views.dashboard),
    path('add_category/',views.add_category),
    path('show_category/',views.show_category),
    path('update_category/<int:category_id>',views.update_category),
    path('delete_category/<int:category_id>',views.delete_category),

    path('add_college/',views.add_college),
    path('show_colleges/', views.show_college),
    path('update_college/<int:college_id>', views.update_college),
    path('delete_college/<int:college_id>', views.delete_college),

    path('show_location_college/',views.show_location_college)


]