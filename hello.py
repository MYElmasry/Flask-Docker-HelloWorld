from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/mo")
def hello_mo():
    return '<p style="color: red">Hello, World from mo!</p>'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
