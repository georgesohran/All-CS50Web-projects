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
        c = 0
        sorted_items_names = sorted(added_items.keys())
        for k in sorted_items_names:
            pv = added_items.pop(k)
            added_items.update(=pv)
        for item in added_items:
            print(added_items[item],item.upper())
        break
    except KeyError:
        break

