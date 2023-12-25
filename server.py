import queue
from flask import Flask, request
from queue import Empty, Queue
from bot import execute_m_clicks
import json

app = Flask(__name__)
clickqueue = Queue();
def exec_queue():
    while not clickqueue.empty():
        execute_m_clicks(clickqueue.get())   
        
@app.route('/')
def hello():
    return 'Bem-vindo ao meu servidor web!'

@app.route('/registry', methods=['GET'])
def registry():
    nome = request.args.get("nome")
    ip = request.args.get("ip")
    data = ["nome", nome, "ip", ip]
    with open("members.json", 'r') as file: 
        dados = json.load(file) 

    dados[nome] = ip 

    with open("members.json", "w") as file:  # Open in write mode to save
        json.dump(dados, file)  # Write the updated data

    return f"Nome: {nome}, IP: {ip} registrado com sucesso."

@app.route('/coord', methods=['GET'])
def regis_queue():
    data = request.get_json();
    coord: list[float] = [data["x"], data["y"]]
    clickqueue.put(coord);
    exec_queue();
    return ["ok", coord[0], coord[1]]
    
app.run(host='0.0.0.0', port=5000)
