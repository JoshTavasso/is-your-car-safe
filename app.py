"""
app.py
The script used for deploying this bot
"""
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	"""Landing Page"""
	return render_template('map.html')

# running server/application
if __name__ == '__main__':
	app.run()
