added_items = {}

def add_item(it):
    added_items[it] = 0

while True :
    try:
        item = input()
        if item not in added_items:
            add_item(item)
        else:
            added_items[item]+=1
    except EOFError:
        for item in added_items:
            print(added_items[item],item)
    except KeyError:
        break

