from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column('First Name', ['Tony', 'Michelle'])
table.add_column('Last Name', ['Ishangu', 'Wambungu'])

table.align = 'l'
print(table)