from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    webapps = [
        {"name": "Weather Station", "url": "http://10.0.0.138:8001", "description": "Weather base station","favicon": "http://10.0.0.138:8001/static/favicon.ico"},
        {"name": "Task-UI", "url": "http://10.0.0.138:8003", "description": "Web front end for the task-api","favicon": "http://10.0.0.138:8003/static/favicon.ico"},
        {"name": "Webapp 3", "url": "http://localhost:5003", "description": "will see you soon Webapp3;)","favicon": "https://example.com/weather-favicon.ico"},
        # Add more webapps as needed
    ]
    return render_template('index.html', webapps=webapps)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8004, debug=True)