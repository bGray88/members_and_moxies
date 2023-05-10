from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members_table/', views.members_table, name='members_table'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
