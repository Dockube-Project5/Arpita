from flask import Flask ,render_template
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('arpita.html')


app.run(debug=True,host='0.0.0.0',port=2000)