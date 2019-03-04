# IS YOUR CAR SAFE?

Do you ever wonder if your car is safe after you parked?

Using Google Maps API and an incident dataset located at https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783, we created a web application that can display incidents near your location and based on the number of incidents, we determine if your parking spot is safe or not!

User can input their location and the application shows them all vehicle-related incidents
such as vehicle thefts. 

Locations are limited to just San Francisco, CA. 

# Built With

Languages: HTML, CSS, Javascript, Python

Frameworks: Flask

API: Google Maps API

# Deployed @ (Temporarily):

https://isyourcarsafe.pythonanywhere.com/

# Authors

Implemented at HackUCI 2019 by:

Joshua Tavassolikhah

David Yip

Justin Leong

Joseph Medina.

# SETUP (If you would like to modify this project):

1. Clone this repository

2. Setup Virtual Environment:
    
    2a. Ensure pip is upgraded

        python3 -m pip install --user --upgrade pip
   
    2b. Install virtualenv

        MAC/Linux:
        
        python3 -m pip install --user virtualenv

        Windows:

        py -m pip install --user virtualenv
    
    2c. Create virtual environment

        MAC/Linux:

        python3 -m virtualenv venv

        Windows:

        py -m virtualenv env

3. Install dependencies:
    
    3a. Activate virtualenv: 
    
        source venv/bin/activate
    
    3b. Install dependencies:
        
        pip install -r requirements.txt

4. Retrieve updated vehicle related incident data set:
    
    4a. Export csv file of all police incidents from https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783
    
    4b. Put csv file into the main project directory and rename to "calls.csv".
    
    4c. Run BuildDataSet.py to create the dataset needed:
        
        python modules/BuildDataSet.py
    
    4d. Vehicle related incident dataset should now be stored in "vehicles.csv", located in the main project directory
    
    5e. Remove "calls.csv" because it is a very large file. :)

# RUNNING THE PROGRAM:

1. Get a Google Maps API Key and add it to templates/map.html

2. Run the following commands:
    
        export FLASK_APP=app.py
        flask run

3. Go to the local server displayed: http://127.0.0.1:5000/


