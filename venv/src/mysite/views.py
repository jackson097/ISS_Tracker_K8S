from django.shortcuts import render
from django.http import HttpResponse
from mysite.db_functions import get_coords_from_db, remove_and_replace_coords, create_table
import requests

iss_api_url = "http://api.open-notify.org/iss-now.json"

def main(request):

    # API calls to get latitude and longitude
    current_iss_latitude = requests.get(iss_api_url).json()['iss_position']['latitude']
    current_iss_longitude = requests.get(iss_api_url).json()['iss_position']['longitude']

    create_table()

    # Get database coordinates
    previous_coords = get_coords_from_db()

    # Remove and replace old coords from db
    remove_and_replace_coords(current_iss_latitude, current_iss_longitude)

    # Format messages to be displayed
    current_coords = "(" + current_iss_latitude + ", " + current_iss_longitude + ")"

    context = {
        "previous_coords":previous_coords,
        "current_coords":current_coords,
        "title":"ISS Tracker"
    }
    
    return render(request, 'base.html', context) 