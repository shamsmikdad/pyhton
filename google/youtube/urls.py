from . import views
from django.urls import path 

urlpatterns = [
    path ("", views.index, name="index"),
    path ("homam", views.homam, name="homam"),
    path ("ali", views.ali, name="ali"),
    path ("<str:name>", views.greet, name="greet"),
]
