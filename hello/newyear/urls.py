from . import views
from django.urls import path

urlpatterns= [
    path("", views.index, name=("index")),
    # path("<str:yourname>", views.gere, name=("gere")),
    path("<int:birthday>", views.age, name=("age")),
    path("mario",views.mario,name=("mario")),   
]