from flask import Flask, render_template, Response, url_for, jsonify
from datetime import datetime
import time
import random
import getMenu
import json

app = Flask(__name__)

lines = []
with open('cheering_phrases.txt', 'r') as f:
    lines = f.readlines()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/time_feed')
def time_feed():
    def generate():
            current_time = datetime.now().strftime("%H:%M:%S")
            current_date = datetime.now().strftime("%d.%m.%Y")
            yield f"{current_time}\n{current_date}"
    return Response(generate(), mimetype='text/plain')

@app.route('/phrases')
def phrases():

    index = random.randint(0, len(lines)-1)
    return Response(f"{lines[index]}", mimetype='text')

@app.route('/menu')
def menu():
    # get data from getMenu.py
    # get only once a day and if error try 5x with 5 min intervals
    # Sunday and Saturday return "No menu today"

    # lisää error caset version ja url metodeihi ja tänne error handle

    date = getMenu.get_date()

    if date[2] == "Sat" or date[2] == "Sun":
        return jsonify({"error": "No menu today"})
    
    version = getMenu.get_version(date)
    url = getMenu.get_url(date, version)

    # restaurant contains res data of all tty restaurants in a list
    menu_data = getMenu.get_restaurants(getMenu.fetchData(url))

    # Convert menu data to a list of dictionaries
    restaurants = []
    for restaurant in menu_data:
        restaurant_info = {
            "name": restaurant.name,
            "open_today": restaurant.open_today,
            "eating_hours": restaurant.eating_hours,
            "menu": restaurant.menu,
        }
        restaurants.append(restaurant_info)

    return jsonify(restaurants)  

    #return Response( json.dumps(restaurants), mimetype='application/json')

app.route('/weather')
def get_weather():
    pass


if __name__ == '__main__':
    app.run(debug=True, threaded=True)