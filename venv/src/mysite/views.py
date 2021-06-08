from django.shortcuts import render
from django.http import HttpResponse
from mysite.db_functions import get_coords_from_db, remove_and_replace_coords
import requests

ISS_API_URL = "http://api.open-notify.org/iss-now.json"

def main(request):

    # API calls to get latitude and longitude
    response_json = requests.get(ISS_API_URL).json()
    current_iss_latitude = response_json['iss_position']['latitude']
    current_iss_longitude = response_json['iss_position']['longitude']

    # Get database coordinates and store into string
    coords = get_coords_from_db()
    if coords == False:
        previous_coords = "N/A"
    else:
        previous_coords = "(" + str(coords[0]) + ", " + str(coords[1]) + ")"

    # Remove and replace old coords from db
    remove_and_replace_coords(current_iss_latitude, current_iss_longitude)

    # Format current coords string to be displayed
    current_coords = "(" + current_iss_latitude + ", " + current_iss_longitude + ")"

    context = {
        "previous_coords":previous_coords,
        "current_coords":current_coords,
        "title":"ISS Tracker"
    }
    
    return render(request, 'base.html', context) 