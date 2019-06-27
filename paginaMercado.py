from flask import Flask, render_template
import database
import reports

app = Flask(__name__)

database = "spiceworks_prod.db"

# create a database connection
conn = reports.create_connection(database)
data = reports.select_closed_tasks_by_client(conn,'PEC', 'Fixo', '2018-09-01','2018-10-01', 80)

#print(data)
#@app.route("/")
@app.route("/relatorio_secreto")
def home():
    return render_template('home.html', data=data)

@app.route("/estoque")
def estoque():
    return render_template('estoque.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
