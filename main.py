class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount: float) -> bool:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self) -> float:
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number: str, account_holder: str) -> bool:
        if account_number in self.accounts:
            return False
        self.accounts[account_number] = BankAccount(account_number, account_holder)
        return True
    
    def get_account(self, account_number: str) -> BankAccount:
        return self.accounts.get(account_number, None)
    
    def deposit_to_account(self, account_number: str, amount: float) -> bool:
        account = self.get_account(account_number)
        if account:
            return account.deposit(amount)
        return False
    
    def withdraw_from_account(self, account_number: str, amount: float) -> bool:
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        return False
    
    def get_balance(self, account_number: str) -> float:
        account = self.get_account(account_number)
        if account:
            return account.get_balance()
        return None


# Beispielcode zur Nutzung des Bankkontosystems

# Erstellung einer Bankinstanz
bank = Bank()

# Erstellung eines neuen Kontos
bank.create_account("123456", "Max Mustermann")

# Einzahlung auf das Konto
bank.deposit_to_account("123456", 100.0)

# Abhebung vom Konto
bank.withdraw_from_account("123456", 50.0)

# Abfrage des Kontostands
balance = bank.get_balance("123456")
print(f"Der Kontostand von Max Mustermann ist: {balance}")
