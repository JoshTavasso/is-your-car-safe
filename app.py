"""
app.py
The script used for deploying this app
"""
from flask import Flask, request, render_template
import GatherIncidents

app = Flask(__name__)

@app.route('/')
def index():
	"""Landing Page"""
	return render_template('map.html')

@app.route('/results', methods = ['POST'])
def get_lat_long(jsdata):
	jsdata = request.form['location']
	with open(jsdata, 'r') as file:
		coordinate_dict = json.load(file)
	return GatherIncidents.create_relevant_incidents(coordinate_dict["lng"], coordinate_dict["lat"], 1) 

# running server/application
if __name__ == '__main__':
	app.run()
