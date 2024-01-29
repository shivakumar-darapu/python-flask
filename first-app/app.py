from flask import Flask, render_template

app = Flask(__name__)
@app.route('/Hello')
def hello():
    return "Hello World!"

@app.route('/Index')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)