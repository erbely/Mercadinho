from flask import Flask, render_template, request
import database
import reports

app = Flask(__name__)

database = "spiceworks_prod.db"

# create a database connection
conn = reports.create_connection(database)
clients = reports.select_all_clients(conn)
data = reports.select_closed_tasks_by_client(conn,'PEC', 'Fixo', '2018-09-01','2018-10-01', 80)
#data = reports.select_closed_tasks_by_client(conn, clients, tipo, data_ini,data_fin, 80)

#print(data)
#@app.route("/")
@app.route("/relatorio_secreto")
def home():
    return render_template('home.html', data=data)

@app.route("/personalizado", methods=['POST', 'GET'])
def personalizado():
    value = request.args.get("client")
    ticket = request.args.get("ticket")
    tipo = request.args.get("tipo")
    print(value, ticket, tipo)
    return render_template('personalizado.html', data=data, clients=clients)

@app.route("/gerencial")
def gerencial():
    return render_template('gerencial.html', data=data)

@app.route("/contratos")
def contratos():
    return render_template('contratos.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
