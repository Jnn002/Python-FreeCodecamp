# Budget app in Python

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.amount = 0

    def __str__(self):
        title = f'{self.category:*^30}\n'
        items = ''
        total = 0
        for item in self.ledger:
            items += f'{item["description"][0:23]:23}{item["amount"]:>7.2f}\n'
            total += item['amount']
        output = title + items + 'Total: ' + str(total)
        return output    
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.amount += amount
        
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.amount += amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self, amount):
        return sum([item['amount'] for item in self.ledger])
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {category.category}'})
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if self.amount < amount:
            return False
    
def create_spend_chart(categories):
    pass


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food) 
