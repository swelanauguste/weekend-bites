import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    is_buyer = models.BooleanField(default=True)


class Location(models.Model):
    location_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("location_name",)

    def __str__(self):
        return self.location_name.title()


class Profile(models.Model):
    GENDER_LIST = [
        ("F", "F"),
        ("M", "M"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_LIST, default=GENDER_LIST[0][0]
    )
    address = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="user_location_list",
        null=True,
        blank=True,
    )
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField("DOB", blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, default="+1")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def get_profile_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"

    def __str__(self) -> str:
        if self.name:
            return f"{self.name}"
        return self.user.email
