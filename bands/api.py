# RiffMates/bands/api.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify

from ninja import Router, ModelSchema

from bands.models import Venue

router = Router()

class VenueOut(ModelSchema):
    slug: str
    url: str
    class Meta:
        model = Venue
        fields = ["id", "name", "description"]

    @staticmethod
    def resolve_slug(obj):
        slug = slugify(obj.name) + "-" + str(obj.id)
        return slug

    @staticmethod
    def resolve_url(obj):
        url = reverse("api-1.0:fetch_venue", args=[obj.id, ])
        return url

@router.get("/venue/{venue_id}/",
    response=VenueOut,
    url_name="fetch_venue")
def fetch_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    return venue

@router.get("/venues/", response=list[VenueOut])
def venues(request, name=None):
    venues = Venue.objects.all()
    if name is not None:
        venues = venues.filter(name__istartswith=name)
    return venues