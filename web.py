#flask website



from flask import Flask, render_template, request
import geo_weather
app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    forecast = None
    if address:
    	forecast = geo_weather.get_weather(address)
    return render_template('index.html', forecast=forecast) #this is what you are returning back

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()


  #use this link to run the above http://127.0.0.1:5000/