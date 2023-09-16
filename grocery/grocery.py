added_items = {}


while True :
    try:
        item = input()
        if item not in added_items:
            add_item(item)
        else:
            
    except EOFError:
        break

def add_item(it):
    added_items[it] = 0