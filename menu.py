""""
menu = [ [ 'Egg Sandwish', 'Bagel', 'Coffee'],
        [ 'Egg Sandwish', 'Bagel', 'Coffee'],
        ['Soup', 'Salad', 'Spaghetti', 'Taco']]

print(menu[0][1])


menus = { 'Breakfast':[ 'Egg Sandwish', 'Bagel', 'Coffee'],
        'Lunch':      [ 'Egg Sandwish', 'Bagel', 'Coffee'],
        'Dinner':     ['Soup', 'Salad', 'Spaghetti', 'Taco']}

print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])

"""

menus = { 'Breakfast':[ 'Egg Sandwish', 'Bagel', 'Coffee'],
        'Lunch':      [ 'Egg Sandwish', 'Bagel', 'Coffee'],
        'Dinner':     ['Soup', 'Salad', 'Spaghetti', 'Taco']}

for name, menu in menus.items():
    print (name, ':', menu)

