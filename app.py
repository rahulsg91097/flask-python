from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HEllo Flask!'

@app.route('/products')
def products():
    return "This is products ka page"

if __name__ == "__main__":
    app.run(debug=True)