from flask import Flask
from flask import render_template

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")


@app.route('/')
def index():
    return render_template('index.html', page_title="collections")

#@app.route('/submit')
#def submit_item():
#   return render_template('submit.html', page_title="Submit")



if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
