from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    END_USER = 'end_user'
    CONTENT_WRITER = 'content_writer'
    ROLES = (
        (END_USER, 'End User'),
        (CONTENT_WRITER, 'Content Writer')
    )

    role = models.CharField(
        choices=ROLES,
        max_length=30,
        default=END_USER,
    )


