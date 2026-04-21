import requests
from config import CLICKUP_TOKEN, LIST_ID

headers = {
    "Authorization": CLICKUP_TOKEN,
    "Content-Type": "application/json"
}

def criar_tarefa_clickup(nome, descricao="", prioridade="normal"):
    prioridade_map = {
        "alta": 1,
        "normal": 3,
        "baixa": 4
    }

    payload = {
        "name": nome,
        "description": descricao,
        "priority": prioridade_map.get(prioridade, 3)
    }

    url = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

    r = requests.post(url, json=payload, headers=headers)

    print("STATUS:", r.status_code)
    print("RESPONSE:", r.text)
    
    return r.json()