from datetime import datetime 

class Transaction:
    def __init__(self, trans_type, amount, category, date=None):
        self.trans_type = trans_type
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "trans_type": self.trans_type,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            trans_type=data["trans_type"],
            amount=data["amount"],
            category=data["category"],
            date=data.get("date")
        )