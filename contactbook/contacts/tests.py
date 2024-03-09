from django.test import TestCase
from .models import ContactInformation

class ContactInformationTestCase(TestCase):

    def setUp(self):
        # Create a sample contact information object for testing
        self.contact_info = ContactInformation.objects.create(
            name="John Doe",
            phone_number="9876543210",
            email="john.doe@example.com",
            address="123 Main Street",
            pincode="45"
        )

    def test_contact_information_creation(self):
        """
        Test if ContactInformation object is created correctly.
        """
        self.assertEqual(self.contact_info.name, "John Doe")
        self.assertEqual(self.contact_info.phone_number, "9876543210")
        self.assertEqual(self.contact_info.email, "john.doe@example.com")
        self.assertEqual(self.contact_info.address, "123 Main Street")
        self.assertEqual(self.contact_info.pincode, "456789")

    def test_phone_number_length(self):
        """
        Test if phone number has a maximum length of 10 characters.
        """
        max_length = ContactInformation._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 10)

    def test_pincode_length(self):
        """
        Test if pincode has a maximum length of 10 characters.
        """
        max_length = ContactInformation._meta.get_field('pincode').max_length
        self.assertEqual(max_length, 10)

    def test_default_values(self):
        """
        Test if default values are set correctly.
        """
        contact_info_default = ContactInformation.objects.create()
        self.assertEqual(contact_info_default.phone_number, "0000000000")
        self.assertEqual(contact_info_default.pincode, "123")
