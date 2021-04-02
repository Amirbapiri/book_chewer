from django.db import models
from django.contrib.auth import get_user_model


class Reviewer(models.Model):
    class ReviewerExperience(models.IntegerChoices):
        BEGINNER = 0, 'Beginner'
        INTERMEDIATE = 1, 'Intermediate'
        EXPERT = 2, 'Expert'

    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.SET_NULL)
    experience = models.SmallIntegerField(
        choices=ReviewerExperience.choices,
        default=ReviewerExperience.BEGINNER
    )

    def __str__(self):
        return self.user.email
