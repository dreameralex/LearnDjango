# RiffMates/bands/urls.py
from django.urls import path
from bands import views
urlpatterns = [
    path('musician/<int:musician_id>/', views.musician, name="musician"),
    path('musicians/', views.musicians, name="musicians"),
    path('restricted_page/', views.restricted_page, name="restricted_page"),
]