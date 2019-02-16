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

@app.route('/results', methods=['GET', 'POST'])
def get_lat_long():
	jsdata = request.get_json(force=True)
	print(jsdata)
	GatherIncidents.create_relevant_indicent_json(float(jsdata["lng"]), float(jsdata["lat"]), 1)
	return 'OK'

# running server/application
if __name__ == '__main__':
	app.run()
