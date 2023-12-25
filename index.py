import json
from httpx import head
import requests
url_debug = "http://127.0.0.1:5000"

with open("members.json", 'r') as file: 
    members = json.load(file)
    
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
    
