from django.db import models
from django.auth.models import User

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    @property
    def email(self) -> str:
        return self.customer.email

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
