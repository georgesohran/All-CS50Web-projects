def camel_to_snake(cam):
    for cer in cam:
        if cer.isupper():
            cer.replace(cer,"_"+cer.lower())
    snk = cam
    return snk

camel = input("camelCase: ")
snake = camel_to_snake(camel)
print("snake_case:",snake)