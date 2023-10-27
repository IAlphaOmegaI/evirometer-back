from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    # Emission factors in kg CO2 equivalent per kilometer for different activities
    emission_factors = {
        'car': 0.2,    # A car emits 0.2 kg CO2 per km
        'bus': 0.1,    # A bus emits 0.1 kg CO2 per km
        'train': 0.05, # A train emits 0.05 kg CO2 per km
        'bike': 0.0,   # Biking is assumed to produce no emissions
        'walk': 0.0,   # Walking is also assumed to produce no emissions
    }

    # Function to calculate carbon emissions
    def calculate_emissions(activity, distance):
        if activity in emission_factors:
            emission_factor = emission_factors[activity]
            emissions = emission_factor * distance
            return emissions
        else:
            return "Activity not found in the database"

    # User input
    activity = 'car'
    distance = 500

    # Calculate carbon emissions
    emissions = calculate_emissions(activity, distance)

    # Display the result
    if isinstance(emissions, str):
        return HttpResponse(emissions)
    else:
        return HttpResponse(emissions)