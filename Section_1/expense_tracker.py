# Pqueño script, para un programa de control de gastos
#* TEMAS A CONSIDERAR, FUNCIONES Y FUNCIONES LAMBDA

# Función para añadir un gasto, su total y su categoría
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Función para imprimir los gastos
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Función para calcular el total de los gastos
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Función para filtrar los gastos por categoría
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
# Función principal
def main():
    expenses = []
    # Ciclo infinito para el menú
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
    # Elección del usuario
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break

# llamado a la función principal
main()