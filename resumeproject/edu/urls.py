from django.urls import path
from . import views
urlpatterns=[
    path('edu/',views.skil ,name='skil'),
]