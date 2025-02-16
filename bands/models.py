from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, null=True)
    def __str__(self):
        return f"Musician(id={self.id}, last_name={self.last_name})"

class Venue(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, null=True)
    def __str__(self):
        return f"Venue(id={self.id}, name={self.name})"

class Room(models.Model):
    name = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    def __str__(self):
        return f"Room(id={self.id}, name={self.name})"

class Band(models.Model):
    name = models.CharField(max_length=20)
    musicians = models.ManyToManyField(Musician)
    def __str__(self):
        return f"Band(id={self.id}, name={self.name})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    musician_profiles = models.ManyToManyField(Musician, blank=True)
    venues_controlled = models.ManyToManyField(Venue, blank=True)

@receiver(user_login_failed)
def track_login_failure(sender, **kwargs):
    username = kwargs["credentials"]["username"]
    url = kwargs["request"].path
    print(f"LOGIN Failure by {username} for {url}")