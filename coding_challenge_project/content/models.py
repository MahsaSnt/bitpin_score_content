from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Content(models.Model):
    title = models.CharField(
        max_length=100
    )
    text = models.TextField()


class Score(models.Model):
    NUMBER_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        related_name='score'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='score'
    )
    number = models.PositiveSmallIntegerField(
        choices=NUMBER_CHOICES,
        null=True,
    )

    class Meta:
        unique_together = ('content', 'user')