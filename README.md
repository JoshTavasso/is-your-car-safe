# HackUCI2019

# IS YOUR CAR SAFE?

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
    
    4c. Run "python3 buildDataSet.py".
    
    4d. Vehicle related incident data set will be stored in "vehicles.csv".
    
    5e. Remove "calls.csv" because it is a very large file. :)
