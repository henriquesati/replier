import queue
from time import sleep
from flask import Flask, request
from queue import Empty, Queue
from bot import execute_m_clicks
from index import add_member
import json

app = Flask(__name__)
clickqueue = Queue();
def exec_queue():
    while not clickqueue.empty():
        execute_m_clicks(clickqueue.get())   
        sleep(0.2) #sleeptime nao testado 
        
@app.route('/')
def hello():
    return 'Bem-vindo ao meu servidor web!'

@app.route('/registry', methods=['GET'])
def registry():
    nome = request.args.get("nome")
    ip = request.args.get("ip")
    fun_ret = add_member([nome, ip])
    return fun_ret

@app.route('/coord', methods=['GET'])
def regis_queue():
    data = request.get_json();
    coord: list[float] = [data["x"], data["y"]]
    clickqueue.put(coord);
    exec_queue();
    return ["ok", coord[0], coord[1]]
    
app.run(host='0.0.0.0', port=5000)
