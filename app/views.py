from django.shortcuts import render
import requests
import io
from django.conf import settings
import os


# Create your views here.

def input(user):
	fname = raw_input "First name: "
	lname = raw_input "Last name: "
	street = raw_input "Street Address: (ie: 200 7th Ave.)"
	cityst = raw_input "City, ST: (ie: New York, NY)"
	zipcode = raw_input "Zipcode: "
	email = raw_input "Email address: "
	phone = raw_input "Area Code + Phone Number: (ie: 555-555-5555)"

	