from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
    # return 'HEllo Flask!'

@app.route('/products')
def products():
    return "This is products ka page"

if __name__ == "__main__":
    app.run(debug=True)