from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import models
import json
from django import forms
from calculator.models import Book

def index(request):
    try:
        request_data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError as e:
        # Handle the JSON decoding error
        return HttpResponse(f"Error decoding JSON: {str(e)}", status=400)
    # Emission factors in kg CO2 equivalent per kilometer for different activities
    emission_factors = {
        'car': 0.2,    # A car emits 0.2 kg CO2 per km
        'bus': 0.1,    # A bus emits 0.1 kg CO2 per km
        'train': 0.05, # A train emits 0.05 kg CO2 per km
        'bike': 0.0,   # Biking is assumed to produce no emissions
        'walk': 0.0,   # Walking is also assumed to produce no emissions
        'cook': 0.4,
    }

    # Function to calculate carbon emissions
    def calculate_emissions(activity, distance,name,description):
        if activity in emission_factors:
            emission_factor = emission_factors[activity]
            emissions = emission_factor * distance
            name=name
            description=description
            return emissions
        else:
            return "Activity not found in the database"

    # User input

    # Calculate carbon emissions
    emissions = calculate_emissions(request_data['activity'], request_data['distance'],request_data['name'],request_data['description'])
    
    john = Book.objects.create(
        name=activity,
        type=activity,
        description=description,
        carbon_emited=emissions
    )

    print(john)
    # output: <Contact: Contact object (1)>

    # Display the result
    if isinstance(emissions, str):
        return HttpResponse(emissions)
    else:
        return HttpResponse(emissions)