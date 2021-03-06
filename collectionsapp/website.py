from flask import Flask
from flask import render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")

app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://matti:E=8)@b*k;"HS,@@localhost.session.sql'

@app.route('/')
def index():
    return render_template('index.html', page_title="collections")

@app.route('/brand')
def brand():
    return render_template('brand.html')

@app.route('/item')
def item():
    return render_template('item.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

#@app.route('/item', methods=['POST'])
#def safe_item_data():
#    if request.method == 'POST':
#        user_submitted_data = 

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
