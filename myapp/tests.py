from django.test import TestCase
from datetime import datetime
from .models import Reservation

# Create your tests here.
class ReservationModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        cls.reservation=Reservation.objects.create(
            first_name='john',
            last_name='McDonald'
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time, datetime)