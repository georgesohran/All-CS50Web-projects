file = input("File name: ").replace(" ","")
i = "image/"
a = ""

if file.endswith("gif"):
    print(i+"gif")
elif file.endswith("jpg"):
    print(i+"jpg")
elif file.endswith("jpeg"):
    print(i+"jpeg")
elif file.endswith("png"):
    print(i+"png")
elif file.endswith("pdf"):
    print(i+"pdf")
elif file.endswith("txt"):
    print(i+"txt")
elif file.endswith("zip"):
    print(i+"zip")
else:
    print("application/octet-stream")

