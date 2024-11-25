from django.test import TestCase, Client
from django.urls import reverse

from .models import Reservation


class ReservationsCoreTestCase(TestCase):
    def test_core(self):
        self.assertEqual(1, 1)


class ReservationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.reservation_url = reverse("reservation-list")

    def test_create_reservation(self):
        data = {
            "customer": "John Doe",
            "facility": "Facility 1",
            "phone": "123-456-7890",
            "datetime_from": "2024-01-01 12:00:00",
            "datetime_to": "2024-01-01 13:00:00",
            "party_size": 4,
        }
        response = self.client.post(self.reservation_url, data, format="json")

        self.assertEqual(response.status_code, 201)

    def test_retrieve_reservation(self):
        reservation = Reservation.objects.create(
            customer="John Doe",
            facility="Facility 1",
            phone="123-456-7890",
            datetime_from="2024-01-01 12:00:00",
            datetime_to="2024-01-01 13:00:00",
            party_size=4,
        )

        response = self.client.get(f"{self.reservation_url}{reservation.id}/")

        self.assertEqual(response.status_code, 200)

    def test_update_reservation(self):
        reservation = Reservation.objects.create(
            customer="John Doe",
            facility="Facility 1",
            phone="123-456-7890",
            datetime_from="2024-01-01 12:00:00",
            datetime_to="2024-01-01 13:00:00",
            party_size=4,
        )
        data = {
            "customer": "Jane Doe",
            "facility": "Facility 2",
            "phone": "987-654-3210",
            "datetime_from": "2024-01-01 14:00:00",
            "datetime_to": "2024-01-01 15:00:00",
            "party_size": 6,
        }

        response = self.client.put(
            f"{self.reservation_url}{reservation.id}/", data, format="json"
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_reservation(self):
        reservation = Reservation.objects.create(
            customer="John Doe",
            facility="Facility 1",
            phone="123-456-7890",
            datetime_from="2024-01-01 12:00:00",
            datetime_to="2024-01-01 13:00:00",
            party_size=4,
        )

        response = self.client.delete(f"{self.reservation_url}{reservation.id}/")
        self.assertEqual(response.status_code, 204)
