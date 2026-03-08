import json
from models import Transaction

def load_transactions():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            return [Transaction.from_dict(entry) for entry in data]
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open("data.json", "w") as f:
        data = [entry.to_dict() for entry in transactions]
        json.dump(data, f, indent=2)