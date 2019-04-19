from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Renann Souza', cpf='12345678912', email='puera@mailinator.com',
                    phone='22123456789')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        """Confirmação de Inscrição"""
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """Email Destinatário"""
        expect = 'contato@eventex.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """Envio de emails"""
        expect = ['contato@eventex.com', 'puera@mailinator.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        """Corpo da msg"""
        contents = [
            'Renann Souza',
            '12345678912',
            'puera@mailinator.com',
            '22123456789'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
