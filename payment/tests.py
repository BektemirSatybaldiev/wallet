from django.test import TestCase
from .models import Customer


class CustomerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(username='johnesbones', first_name='john', last_name='johnes', email='blabla@mail.ru',
                                date_of_birth='1988-10-21', verified=False)

    def test_username_content(self):
        customer = Customer.objects.get(id=1)
        expected_obj_username = f'{customer.username}'
        self.assertEqual(expected_obj_username, 'johnesbones')

    def test_email(self):
        customer = Customer.objects.get(id=1)
        expected_email_pattern = f'{customer.email}'
        self.assertEqual(expected_email_pattern, 'blabla@mail.ru')
