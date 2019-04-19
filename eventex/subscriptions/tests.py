from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
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
        """Deve conter todos os argumentos do form"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Deve conter o CSRF no form"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """O Contexto deve ter o subscription form"""
        self.assertIsInstance(self.form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form deve conter 4 campos"""
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))


class SubscribePostTest(TestCase):
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

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com'

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com', 'renann_puera@hotmail.com']

        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Renann Souza', email.body)
        self.assertIn('12345678912', email.body)
        self.assertIn('renann_puera@hotmail.com', email.body)
        self.assertIn('22997903545', email.body)


class SubscribeInvalidPost(TestCase):
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
