# -----------/ SCOPE /--------------
# 
enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside function {enemies}')

increase_enemies()
print(f'enemies outside the function {enemies}')

# LOCAL SCOPE
# Variables defined inside a function
def drink_portion():
    portion = 2
    print(portion)

drink_portion()

# GLOBAL SCOPE
# Variables declared outside a function

health = 10
def drinks():
    strength = 2
    print(health)
    # global variables can be accessed inside a function
drinks()