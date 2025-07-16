from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample car data
cars = [
    {"name": "Honda City", "price": 900000, "fuel": "Petrol"},
    {"name": "Hyundai Creta", "price": 1300000, "fuel": "Diesel"},
    {"name": "Maruti Swift", "price": 800000, "fuel": "Petrol"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cars')
def view_cars():
    return render_template('cars.html', cars=cars)

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        name = request.form['name']
        price = int(request.form['price'])
        fuel = request.form['fuel']
        cars.append({"name": name, "price": price, "fuel": fuel})
        return redirect(url_for('view_cars'))
    return render_template('add_car.html')

@app.route('/search_car', methods=['GET', 'POST'])
def search_car():
    if request.method == 'POST':
        query = request.form['query'].lower()
        result = [car for car in cars if query in car['name'].lower()]
        return render_template('search_car.html', cars=result)
    return render_template('search_car.html', cars=[])

@app.route('/suggest_car', methods=['GET', 'POST'])
def suggest_car():
    suggestions = []
    if request.method == 'POST':
        budget = int(request.form['budget'])
        fuel = request.form['fuel']
        suggestions = [car for car in cars if car['price'] <= budget and car['fuel'].lower() == fuel.lower()]
    return render_template('suggest_car.html', cars=suggestions)

@app.route('/select_car/<car_name>')
def select_car(car_name):
    car = next(car for car in cars if car['name'] == car_name)
    return render_template('selected_car.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/static-test')
def static_test():
    return f'<link rel="stylesheet" href="{url_for("static", filename="styles.css")}">This page should have styles applied if static works.'
