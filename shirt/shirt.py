import sys
import os
import PIL

def main():
    try:
        check_input()

        before = sys.argv[1]
        after = sys.argv[2]

        shirt = PIL.Image.open("shirt.png")
        image = PIL.Image.open(before)
        nsize = shirt.size
        PIL.ImageOps.fit(image, nsize)
        image.paste(shirt)
        image.save(after)


    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_input():
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    _,extention1 = sys.argv[1].split(".")
    _,extention2 = sys.argv[2].split(".")

    if extention1 != extention2:
        sys.exit("Input and output have different extensions")
    if extention2 == "png" or extention2 == "jpg" or extention2 == "jpeg":
        pass
    else:
        sys.exit("Invalid output")

main()