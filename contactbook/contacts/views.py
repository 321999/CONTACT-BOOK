from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseBadRequest
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
    # print(data)
    # print("*"*10)
    if request.GET.get("contact_search"):
        data=data.filter(name__icontains=request.GET.get("contact_search"))
        print("*"*5+request.GET.get("contact_search"))             
    # To show send the data from backend to frontend we use context keyword 
    return render(request,"displaycontact.html",context={"data":data})
    # return  HttpResponse("completing the projgrje")

def update_contact(request,id):
    record_to_be_update=ContactInformation.objects.get(id=id)
    if request.POST:

        data=request.POST

        record_to_be_update.name=data.get("NameOfPeople")
        # record_to_be_update.phone_number=data.get("phone")
        record_to_be_update.email=data.get("email")
        record_to_be_update.address=data.get("Address")
        phone_number = data.get("PhoneNumberOfPeople")

        if phone_number is not None and phone_number.isdigit() and len(phone_number) == 10:
            record_to_be_update.phone_number = phone_number
            record_to_be_update.save()
            return redirect("/show_contact/")
        else:
            return HttpResponseBadRequest("Invalid phone number format")

    return render(request,"updatecontact.html",context={"backend_data":record_to_be_update})


# from django.http import HttpResponseBadRequest

# def update_contact(request, id):
    record_to_be_update = ContactInformation.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        # Update name, email, and address unconditionally
        record_to_be_update.name = data.get("NameOfPeople")
        record_to_be_update.email = data.get("email")
        record_to_be_update.address = data.get("Address")

        # Check and update phone_number only if a valid value is provided
        phone_number = data.get("phone")

        if phone_number is not None and phone_number.isdigit() and len(phone_number) == 10:
            record_to_be_update.phone_number = phone_number
            record_to_be_update.save()
            return redirect("/show_contact/")
        else:
            return HttpResponseBadRequest("Invalid phone number format")

    return render(request, "updatecontact.html", context={"backend_data": record_to_be_update})



def delete_contact(request,id):
    record_to_be_delete=ContactInformation.objects.get(id=id)  
    print("the id of which location is added is",record_to_be_delete)    

    record_to_be_delete.delete() 
    # print("deleted the record")  
    # record_to_be_delete.save()
    return redirect("/show_contact/")
    # return HttpResponse("object deleted")     

def home_page(request):
    return render(request,"home.html")