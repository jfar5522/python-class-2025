class Customer:
    #initializes class attribute variables
    def __init__(self, accountNumber, amount):
        self._accountNumber = accountNumber
        self._amount = amount
    
    #returns the string of what the class is made up of
    def __str__(self):
        return f"{self._accountNumber},{self._amount}"
    
    #does the same thing as __str__ except for lists instead of individual class calls
    def __repr__(self):
        return f"{self._accountNumber},{self._amount}"

    #takes the inputed interestpct number and multiplies it by the class amount to create the percentage amount.
    #the percent amount is then added to the class amount. Class amount is returned to easily access the change if need be.
    def calculateInterestPayment(self, interestPct):
        interestPct *= .01

        try:
            #makes sure the amount is a float, if not exit function
            self._amount = float(self._amount)
            pctAmount = round((self._amount + (self._amount * interestPct)), 2)
        except ValueError:
            return
        
        self._amount = pctAmount
        return self._amount #here to use for convience :)
    
