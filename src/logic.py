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

def get_balance(transactionList):
    income = 0
    expense = 0

    for transaction in transactionList:
        if(transaction.trans_type == "income"):
            income += transaction.amount
        elif(transaction.trans_type == "expense"):
            expense += transaction.amount

    Balance = income - expense
    return Balance