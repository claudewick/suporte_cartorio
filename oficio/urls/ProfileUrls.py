from django.urls import path
from oficio.views.ProfileView import list_profile_view

urlpatterns = [
    path("", list_profile_view, name='profiles'),
    path("<int:id>", list_profile_view, name='profiles'),
]
