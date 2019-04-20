from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                           name='Renann Souza',
                           cpf='12345678912',
                           email='puera@mailinator.com',
                           phone='22123456789')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription deve ter a auto created at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)
