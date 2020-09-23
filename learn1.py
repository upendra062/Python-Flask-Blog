from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    # return 'Hello, World!'
    return render_template('index.html')

@app.route("/about")
def Rocky():
    upendra = "Master Rocky"
    return render_template('about.html', Hero=upendra)

app.run(debug=True)