from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionTestForm(TestCase):
    def test_form_has_fields(self):
        """Form deve conter 4 campos"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']

        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """o campo CPF deve conter só números"""
        form = self.make_validated_form(cpf='ABCD5678912')

        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """O campo CPF deve conter 11 digitos"""
        form = self.make_validated_form(cpf='1234')

        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]

        self.assertListEqual([msg], errors_list)

    @staticmethod
    def make_validated_form(**kwargs):
        """O campo CPF deve conter 11 digitos"""
        valid = dict(name='Renann Souza', cpf='12345678912',
                     email='puera@mailinator.com', phone='22123456')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
