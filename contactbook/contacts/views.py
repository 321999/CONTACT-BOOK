from django.shortcuts import render,redirect
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

def show_contact(request):
    data=ContactInformation.objects.all()
    print(data)
    # To show send the data from backend to frontend we use context keyword 
    return render(request,"displaycontact.html",context={"data":data})
    return  HttpResponse("completing the projgrje")

def update_contact(request,id):
    record_to_be_update=ContactInformation.objects.get(id=id)
    if request.POST:

        data=request.POST

        record_to_be_update.name=data.get("NameOfPeople")
        record_to_be_update.phone_number=data.get("phone")
        record_to_be_update.email=data.get("email")
        record_to_be_update.address=data.get("Address")

        record_to_be_update.save()

        return redirect("/show_contact/")
    return render(request,"updatecontact.html")

def delete_contact(request,id):
    record_to_be_delete=ContactInformation.objects.get(id=id)

    record_to_be_delete.delete()
    return redirect(request,"/show_contact/")

    