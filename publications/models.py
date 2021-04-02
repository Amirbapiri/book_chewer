from django.db import models

from django.contrib.auth import get_user_model


class Publication(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=125, blank=False, null=False)
    reg_number = models.CharField(max_length=12, blank=False, null=False)
    date_of_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Publication {str(self.name)}"
