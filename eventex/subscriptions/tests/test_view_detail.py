from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Renann Souza',
            cpf='12345678912',
            email='puera@mailinator.com',
            phone='22123456'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))
        self.subscription = self.resp.context['subscription']

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        self.assertIsInstance(self.subscription, Subscription)

    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.email,
            self.obj.phone)
        for content in contents:
            with self.subTest():
                self.assertContains(self.resp, content)


class SubscriptionDetailNotFound(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/0/')

    def test_not_found(self):
        self.assertEqual(404, self.resp.status_code)
