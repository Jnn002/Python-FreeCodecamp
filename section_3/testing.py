# Budget app, testing
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

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

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.category}'):
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

def create_spend_chart(categories):
    total_spent = 0
    spent_category = []
    
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent -= item['amount']
        spent_category.append(spent)
        total_spent += spent
        
    porcentajes = [int((spent/total_spent)*100) // 10 * 10 for spent in spent_category]
    
    chart = 'Percentage spent by category\n'
    
    for i in range(100, -1, -10):
        chart += f'{i:>3}| '
        for percentage in porcentajes:
            if percentage >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    
    chart += '    -' + '---'*len(categories) + '\n'
    
    max_length = max([len(category.category) for category in categories])
    for i in range(max_length):
        chart += '     '
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + '  '
            else:
                chart += '   '
        chart += '\n'
    return chart.strip('\n')
        
food = Category('food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.withdraw(25, 'clothes')
food.transfer(20, clothing)
Groceries = Category('Groceries')

food.transfer(50, clothing)
food.check_funds(20)
print(food)

categories = [food, clothing, Groceries]
graph = create_spend_chart(categories)
print(graph)