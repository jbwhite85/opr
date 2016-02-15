from django.shortcuts import render
import requests
import io
from django.conf import settings
import os

# Create your views here.

fname = input("First name: ")
lname = input("Last name: ")
street = input("Street Address: (ie: 200 7th Ave.)")
cityst = input("City, ST: (ie: New York, NY)")
zipcode = input("Zipcode: ")
email = input("Email address: ")
phone = input("Area Code + Phone Number: (ie: 555-555-5555)")

print (fname, lname)
print (street)
print (cityst, zipcode)
print (email)
print (phone)

print ("Please ensure all of your information correct?  ")
