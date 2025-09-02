from flask import Flask, render_template
import requests, os

app = Flask(__name__)
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://backend:5000/api/data')

@app.route('/')
def index():
    try:
        resp = requests.get(BACKEND_URL, timeout=3)
        data = resp.json()
    except Exception as e:
        data = {'error': str(e)}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
