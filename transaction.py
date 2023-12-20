class Transaction:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, user, book, action):
        transaction = {
            'User': user.name,
            'Book': book.title,
            'Action': action
        }
        self.transactions.append(transaction)

    def generate_transaction_report(self):
        print("Transaction Report:")
        for transaction in self.transactions:
            print(f"User: {transaction['User']}, Book: {transaction['Book']}, Action: {transaction['Action']}")
