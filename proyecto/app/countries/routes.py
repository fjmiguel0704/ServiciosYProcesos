from flask import Blueprint, jsonify

countriesBP = Blueprint("countries", __name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
    ]

def _findNextId():
    return max (country["id"] for country in countries) + 1

@countriesBP.route('/')
def index ():
    return 'Hola a todos! :)'

@countriesBP.get("/countries")
def get_countries():
    return jsonify(countries)

@countriesBP.get("/countries/<int:id>")
def getCountry(id):
    for country in countries:
        if country["id"]==id:
            return country, 200
    return{"error": "Country not found"}, 404

@countriesBP.post("/countries")
def addCountry():
    if request.is_json:
        country = request.get_json()
        country["id"] = _findNextId()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__=='__main__':
    countriesBP.run(debug=True, host='0.0.0.0', port=5050)
