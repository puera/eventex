from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
        self.form = self.response.context['form']

    def test_get(self):
        """GET /inscricao deve retornar status code 200"""
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        """Deve retorna a template subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')

    def test_html(self):
        """Deve conter todos os argumentos do form"""
        self.assertContains(self.response,'<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Deve conter o CSRF no form"""
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_has_form(self):
        """O Contexto deve ter o subscription form"""
        self.assertIsInstance(self.form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form deve conter 4 campos"""
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))
