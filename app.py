import flask
from flask import Flask, render_template
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
	app.run(debug=True)

#https://soshace.com/how-i-built-an-admin-dashboard-with-python-flask/
#https://betterprogramming.pub/building-your-first-website-with-flask-part-2-6324721be2ae
#https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
#https://pythonhow.com/adding-more-pages-to-the-website/