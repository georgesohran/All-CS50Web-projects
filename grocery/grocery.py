added_items = {}

def add_item(it):
    added_items[it] = 0

while True :
    try:
        item = input()
        if item not in added_items:
            add_item(item)
            added_items[item]+=1
        else:
            added_items[item]+=1
    except EOFError:
        sorted_keys = sorted(added_items.items())
        for k in sorted_keys:
            added_items[]
        for item in added_items:
            print(added_items[item],item.upper())
        break
    except KeyError:
        break

