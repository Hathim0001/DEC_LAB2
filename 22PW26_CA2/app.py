from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.form.get('name')  
    if name == 'monthly':
        url = "https://meteostat.p.rapidapi.com/point/monthly"
        querystring = {
            "lat": "52.5244",
            "lon": "13.4105",
            "alt": "43",
            "start": "2020-01-01",
            "end": "2020-12-31"
        }

        headers = {
            "x-rapidapi-key": "9e26670594msh919c7c8cb102ce0p10ed43jsn7970e9f69f53",
            "x-rapidapi-host": "meteostat.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', data=data)  
        else:
            return f"Error: {response.status_code}, {response.text}"    
    elif name == 'hourly':
        url = "https://meteostat.p.rapidapi.com/stations/hourly"

        querystring = {"station":"10637","start":"2020-01-01","end":"2020-01-01","tz":"Europe/Berlin"}

        headers = {
	        "x-rapidapi-key": "9e26670594msh919c7c8cb102ce0p10ed43jsn7970e9f69f53",
	        "x-rapidapi-host": "meteostat.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', data=data)  
        else:
            return f"Error: {response.status_code}, {response.text}"    
    elif name == 'daily':
        url = "https://meteostat.p.rapidapi.com/stations/daily"
        querystring = {"station":"10637","start":"2020-01-01","end":"2020-01-31"}

        headers = {
    	    "x-rapidapi-key": "9e26670594msh919c7c8cb102ce0p10ed43jsn7970e9f69f53",
	        "x-rapidapi-host": "meteostat.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', data=data)  
        else:
            return f"Error: {response.status_code}, {response.text}"  
    elif name=='station_climate':
        url = "https://meteostat.p.rapidapi.com/stations/normals"

        querystring = {"station":"10637","start":"1961","end":"1990"}

        headers = {
	        "x-rapidapi-key": "9e26670594msh919c7c8cb102ce0p10ed43jsn7970e9f69f53",
	        "x-rapidapi-host": "meteostat.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', data=data)  
        else:
            return f"Error: {response.status_code}, {response.text}"   
    elif name=='station_meta':
        url = "https://meteostat.p.rapidapi.com/stations/meta"

        querystring = {"id":"10637"}

        headers = {
	        "x-rapidapi-key": "9e26670594msh919c7c8cb102ce0p10ed43jsn7970e9f69f53",
	        "x-rapidapi-host": "meteostat.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', data=data)  
        else:
            return f"Error: {response.status_code}, {response.text}"
    elif name=='nearby_stations':
        url = "https://meteostat.p.rapidapi.com/stations/nearby"

        querystring = {"lat":"51.5085","lon":"-0.1257"}

        headers = {
	        "x-rapidapi-key": "9e26670594msh919c7c8cb102ce0p10ed43jsn7970e9f69f53",
        	"x-rapidapi-host": "meteostat.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', data=data)  
        else:
            return f"Error: {response.status_code}, {response.text}"
    return render_template('index.html') 
 

if __name__ == '__main__':
    app.run(debug=True,port=8000)



