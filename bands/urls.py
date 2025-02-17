# RiffMates/bands/urls.py
from django.urls import path
from bands import views
urlpatterns = [
    path('musician/<int:musician_id>/', views.musician, name="musician"),
    path('musicians/', views.musicians, name="musicians"),
    path('edit_musician/<int:musician_id>/', views.edit_musician, name="edit_musician"),
    path('add_musician/', views.edit_musician, name="add_musician"),
    path('bands/', views.bands, name="bands"),
    path('band/<int:band_id>/', views.band, name="band"),
    path('venues/', views.venues, name="venues"),
    path('add_venue/', views.edit_venue, name="add_venue"),
    path('edit_venue/<int:venue_id>', views.edit_venue, name="edit_venue"),
    path('restricted_page/', views.restricted_page, name="restricted_page"),
    path('musician_restricted/<int:musician_id>/', views.musician_restricted, name="musician_restricted"),
    path(
        "venues_restricted/", views.venues_restricted, name="venues_restricted"
    ),

]