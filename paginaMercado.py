from flask import Flask, render_template
import database
app = Flask(__name__)

data = database.read_json("estoque.json")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',titulo = "Home")

@app.route("/estoque")
def estoque():
    return render_template('estoque.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
