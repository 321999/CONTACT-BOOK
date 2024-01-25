from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
# logic for adding the contact details 
def add_contact(request):
    print("adding the details")
    if request.method=="POST":
        data=request.POST
        # storing  the data to db
        ContactInformation.objects.create(
    # To store the name
        name=data.get("NameOfPeople"),

    # To store the phone numbers as we know phone number is only of 10 digits
        phone_number=data.get("phone"),

    # To store the email
        email=data.get("email"),

    # To store the address
        address=data.get("Address")
    )

        print(data.get("phone"))
        print("value can be fetched")
    return render(request,"addcontact.html")               