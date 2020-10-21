from django.contrib import admin
from django.urls import path, include
from .views import (
    Departamentoslist,
    DepartamentosCreate,
    DepartamentosUpdate,
    DepartamentosDelete,
)

urlpatterns = [
    path('list/', Departamentoslist.as_view(), name='list_departamentos'),
    path('novo/', DepartamentosCreate.as_view(), name='create_departamentos'),
    path('update/<int:pk>/', DepartamentosUpdate.as_view(), name='update_departamentos'),
    path('delete/<int:pk>/', DepartamentosDelete.as_view(), name='delete_departamentos'),

]
