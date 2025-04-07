class Paycheck:
    def __init__(self,amt):
        self.amount = amt
    def __str__(self):
        return f"Paycheck has ${self.amount:,.2f}"
    def __add__(self, other):
        self.amount+=other.amount
    def __sub__(self, other):
        self.amount-=other.amount

