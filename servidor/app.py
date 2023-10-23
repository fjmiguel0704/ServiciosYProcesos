from flask import*

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
    ]

def _findNextId():
    return max (country["id"] for country in countries) + 1

@app.route('/')
def index ():
    return 'Hola a todos! :)'

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/countries/<int:id>")
def getCountry(id):
    for country in countries:
        if country["id"]==id:
            return country, 200
    return{"error": "Country not found"}, 404

@app.post("/countries")
def addCountry():
    if request.is_json:
        country = request.get_json()
        country["id"] = _findNextId()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

