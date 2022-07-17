from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_base, name = "is_name_even_necessary")
]
