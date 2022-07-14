from django.urls import path
from oficio.views.HomeView import home_view

urlpatterns = [
    path("", home_view),
]
