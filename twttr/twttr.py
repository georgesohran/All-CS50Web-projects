def convert(w):
    for c in w:
        if c=="a"or"e"or"u"or"i"or"o":
            w = w.replace(c,"")
    return w

word = input("Input: ").lower()
word = convert(word)
print("Output:",word)