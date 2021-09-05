from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    bio = models.TextField(default="Write some details about yourself", blank=True, null=True)
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")

    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )

    birthday = models.DateField(null = True)

    def get_absolute_url(self):
        return reverse("users:userprofile", kwargs={"pk": self.pk})