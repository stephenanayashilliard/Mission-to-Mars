# Dependencies
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Define the rout for the HTML page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

#Next route and function
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   #mars_data = scrapemars.scrape_all()
   mars_data = scrape_mars.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

if __name__ == "__main__":
   print("I am running")
   app.run()