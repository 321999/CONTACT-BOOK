from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# logic for adding the contact details 
def add_contact(self):
    print("adding the details ")
    return HttpResponse("ADD NEW CONTACT ")