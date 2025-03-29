class Customer:
    def __init__(self, accountNumber, amount):
        self._accountNumber = accountNumber
        self._amount = amount
    
    def __str__(self):
        return f"{self._accountNumber},{self._amount}"
    
    def __repr__(self):
        return f"{self._accountNumber},{self._amount}"

    def calculateInterestPayment(self, interestPct):
        interestPct *= .01

        try:
            self._amount = float(self._amount)
            calculation = round((self._amount + (self._amount * interestPct)), 2)
        except ValueError:
            return
        self._amount = calculation

        return self._amount #here to use for convience :)
    
