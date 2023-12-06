from django.db import models
from registration.models import Customer, Organisation

class Booking(models.Model):
    guest = models.ForeignKey(Customer, on_delete = models.CASCADE)
    place = models.ForeignKey(Organisation, on_delete = models.CASCADE)
    table = models.IntegerField()
    booking_time = models.DateTimeField()

    def __str__(self):
        return f"Бронирование {self.id} для {self.guest} в {self.place}"

