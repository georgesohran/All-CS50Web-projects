added_items = {}

def add_item(item):
    if item not in added_items:
        added_items[item] = 0
        added_items[item] += 1
    else:
        added_items[item] += 1


while True :
    try:
        item = input()
        add_item(item)
    except EOFError:
        for item in added_items:
            print(added_items[item],item.upper())
        break
    except KeyError:
        break

