added_items = {}

def add_item(item):
    if item not in added_items:
        added_items[item] = 1
    else:
        added_items[item] += 1


while True :
    try:
        item = input()
        add_item(item)
    except EOFError:
        added_items_names = sorted(added_items.keys())
        for k in added_items_names:
            pk = added_items.pop(k)
            added_items.update(p=pk)
        for item in added_items:
            print(added_items[item],item.upper())
        break
    except KeyError:
        break

