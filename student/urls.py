from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('delete/<int:id>',views.deleteData , name="delete"),
    path('edit/<int:id>',views.editData , name="edit"),
]
