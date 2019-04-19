from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
        self.form = self.response.context['form']

    def test_get(self):
        """GET /inscricao deve retornar status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Deve retorna a template subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Deve conter todos os tags do form"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Deve conter o CSRF no form"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """O Contexto deve ter o subscription form"""
        self.assertIsInstance(self.form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Renann Souza', cpf='12345678912', email='renann_puera@hotmail.com',
                    phone='22997903545')
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """Post válido deve redirecionar para /inscricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_subscribe_email(self):
        """Deve enviar o e-mail de inscrição"""
        self.assertEqual(1, len(mail.outbox))


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})
        self.form = self.response.context['form']

    def test_post(self):
        """POST inválido não deve redirecionar"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        self.assertIsInstance(self.form, SubscriptionForm)

    def test_has_errors(self):
        self.assertTrue(self.form.errors)


class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Renann Souza', cpf='12345678912', email='renann_puera@hotmail.com',
                    phone='22997903545')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')
