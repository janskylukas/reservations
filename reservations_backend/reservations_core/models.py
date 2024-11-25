from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    street = models.CharField(max_length=100, verbose_name=_("street and number"))
    city = models.CharField(max_length=100, verbose_name=_("city"))
    country = models.CharField(max_length=100, verbose_name=_("country"))
    zip_code = models.CharField(max_length=10, verbose_name=_("zip code"))

    def __str__(self):
        return f"{self.street} {self.city} {self.country}"


class Customer(models.Model):
    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer",
        verbose_name=_("user"),
    )

    phone_number = PhoneNumberField(verbose_name=_("phone number"), region="CZ")

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="customers",
        verbose_name=_("address"),
    )

    social_number = models.CharField(max_length=20, verbose_name=_("social number"))

    @property
    def email(self) -> str:
        return self.username

    @property
    def name(self) -> str:
        """Return full name of the customer"""
        return self.get_full_name()

    def __str__(self) -> str:
        return self.name


class Facility(models.Model):
    class Meta:
        verbose_name = _("facility")
        verbose_name_plural = _("facilities")
    
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(verbose_name=_("description"))
    image = models.ImageField(
        upload_to="facilities", null=True, blank=True, verbose_name=_("image")
    )
    price: float = models.FloatField(verbose_name=_("price per day"))

    def __str__(self):
        return self.name


class Reservation(models.Model):
    class Meta:
        verbose_name = _("reservation")
        verbose_name_plural = _("reservations")

    customer: Customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name=_("customer"),
    )
    facility: Facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name=_("facility"),
    )
    phone = models.CharField(max_length=20, verbose_name=_("phone number"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    datetime_from: datetime = models.DateTimeField(verbose_name=_("datetime from"))
    datetime_to: datetime = models.DateTimeField(verbose_name=_("datetime to"))
    party_size = models.IntegerField(verbose_name=_("party size"))

    @property
    def email(self) -> str:
        return self.customer.email

    @property
    def customer_name(self) -> str:
        return self.customer.name

    @property
    def facility_name(self) -> str:
        return str(self.facility)

    @property
    def days(self) -> int:
        return (self.datetime_to.date() - self.datetime_from.date()).days

    @property
    def price(self) -> float:
        return self.days * self.facility.price

    def __str__(self) -> str:
        return f"{self.customer_name}: {self.datetime_from} - {self.datetime_to}"

    def __repr__(self):
        return "<Reservation: {}>".format(self)
