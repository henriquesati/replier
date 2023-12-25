import json
from typing import Any
from httpx import head
import requests
url_debug = "http://127.0.0.1:5000"

with open("members.json", 'r') as file: 
    members = json.load(file)

def add_member(member: list[Any]):
    with open("members.json", 'r') as file: 
        dados = json.load(file) 
    dados[member[0]] = member[1]
    with open("members.json", "w") as file: 
        json.dump(dados, file)  
    return f"Nome: {member[0]}, IP: {member[1]} registrado com sucesso."
    
def pass_mouse_coord(par: list[float]):
    for key in members:
        url = f"http{members[key]}/5000"
        headers = {
            "Content-Type": "application/json",
            }
        body = {
            "name": key,
            "ip": members[key],
            "x": par[0],
            "y": par[1]
        }
        response = requests.get(f"{url_debug}/coord", json=body, headers=headers)
        print(response)
        return f"{response}"


for key in members:
    print(f"{key}--> {members[key]}")
    
