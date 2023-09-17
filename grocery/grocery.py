added_items = {}

def add_item(item):
    if item not in added_items:
        added_items[item] = 1
    else:
        added_items[item] += 1

def sort_and_print_items():
    sorted_items_names = sorted(added_items.keys())
    for k in sorted_items_names:
        added_items[k] = added_items.pop(k)
    for item in added_items:
        print(added_items[item],item.upper())

while True :
    try:
        item = input()
        add_item(item)
    except EOFError:
        sort_and_print_items()
        break
    except KeyError:
        break

