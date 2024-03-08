from django.db import models

# Create your models here.
# here is database will enter

'''
Contact Information: Store name, phone number, email, and address for each contact.
'''
class ContactInformation(models.Model):
    
    # To store the name
    name=models.CharField(max_length=50)

    # To store the phone numbers as we know phone number is only of 10 digit 
    phone_number = models.CharField(max_length=10, default='0000000000') 

    # To store the email 
    email=models.EmailField()

    # To store address 
    address=models.TextField()  

    # to store the pincode
    pincode=models.CharField(max_length=10,default="123")

