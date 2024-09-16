from flask import Flask, render_template, request
from weather import fetch_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'e15f280201f88f9ba43bb5e60470da9b'  
        weather = fetch_weather(city, api_key)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)