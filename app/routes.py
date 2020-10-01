from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/cars')
def cars():
    car_list = ["BMW", "Audi", "Mercedes", "AMG"]
    return render_template('cars.html', car_list=car_list)


@app.route('/carinfo')
def carinfo():
    info = {
        "name":"BMW Test",
        "make":"German BMW",
        "description": "The newest BMW in the line",
        "events": ["Track Day 1", "Track Day 2"]
    }
    return render_template('carinfo.html', info=info)


@app.route('/newcar')
def newcar():

    return render_template("newcar.html")






