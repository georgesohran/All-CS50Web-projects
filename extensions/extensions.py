file = input("File name: ").replace(" ","")

if file.endswith("gif"):
    print("image/gif")
elif file.endswith("jpeg") or file.endswith("jpg"):
    print("image/jpeg")
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

