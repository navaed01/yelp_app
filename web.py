#flask website



from flask import Flask, render_template, request
import yelp_api
import os
app = Flask(__name__)

@app.route("/")
def index():
    place = request.values.get('place')
    businesses  = None
    if place:
    	businesses  = yelp_api.get(place)
    return render_template('index.html', businesses =businesses, place = place ) #this is what you are returning back
 
@app.route('/about')
def about():
    return render_template('about.html')


#before heroku
# if __name__ == "__main__":
#     app.run()


#FOR heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


  #use this link to run the above http://127.0.0.1:5000/