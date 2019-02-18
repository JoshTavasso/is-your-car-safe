"""
app.py
The script used for deploying this app
"""
from flask import Flask, request, render_template
from modules import GatherIncidents
import json

app = Flask(__name__)

@app.route('/')
def index():
	"""Landing Page"""
	return render_template('map.html')

@app.route('/results', methods=['GET', 'POST'])
def get_lat_long():
	if request.method == 'POST':
		jsdata = request.get_json(force=True)
		print(jsdata)
		GatherIncidents.create_relevant_indicent_json(float(jsdata["lng"]), float(jsdata["lat"]), float(jsdata["radius"]))
		return 'POST'
	else:
		with open('relevant_incidents.json', 'r') as file:
			data = json.loads(file.read())
		return json.dumps(data)
		
# running server/application
if __name__ == '__main__':
	app.run()
