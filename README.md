# HackUCI2019

# IS YOUR CAR SAFE?

Do you ever wonder if your car is safe after you parked?

Using Google Maps API and an incident dataset located at https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783, we created an application that can display incidents near your location and based on the number of incidents, we determine if your parking spot is safe or not!

User can give their location, and the application shows them all vehicle-related incidents, given a radius,
such as vehicle thefts.

Implemented with HTML, CSS, Javascript, Python, and Flask. 

Locations are limited to just San Francisco, CA. 

# SETUP

1. Clone this repository

2. Setup Virtual Environment:
    
    2a. Ensure pip is upgraded

        python3 -m pip install --user --upgrade pip
   
    2b. Install virtualenv

        MAC:
        python3 -m pip install --user virtualenv

        Windows:

        py -m pip install --user virtualenv
    
    2c. Create virtual environment

        MAC:

        python3 -m virtualenv venv

        Windows:

        py -m virtualenv env

3. Install dependencies:
    
    3a. Activate virtualenv: source venv/bin/activate
    
    3b. pip install -r requirements.txt

4. Retrieve updated vehicle related incident data set:
    
    4a. Export csv file of all police incidents from https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783
    
    4b. Put csv file into project folder and rename to "calls.csv".
    
    4c. Run python BuildDataSet.py
    
    4d. Vehicle related incident data set will be stored in "vehicles.csv".
    
    5e. Remove "calls.csv" because it is a very large file. :)

# RUNNING THE PROGRAM:

1. Get a Google Maps API Key and add it to templates/map.html

2. Run the following commands:

    export FLASK_APP=app.py
    flask run

3. Go to the local server displayed: http://127.0.0.1:5000/