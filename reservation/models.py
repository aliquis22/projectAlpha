from django.db import models
from registration.models import Customer, Organisation


class Reservation(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)
    table = models.PositiveIntegerField(default=None)  # default=None, чтобы избежать ошибки с non-nullable полем
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name} {self.organisation.name} {self.time}'