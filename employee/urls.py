from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_emp, name="delete_emp"),
    path('update/<int:id>/', views.update_emp, name="update_emp"),
]
