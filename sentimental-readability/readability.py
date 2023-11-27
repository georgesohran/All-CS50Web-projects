def main():

    text = str(input("Text: "))

    sentances = count_sentances(text)
    words = count_words(text)
    letters = count_letters(text)

    print(f"{sentances}--{words}--{letters}")



def count_sentances(txt:str):
    count = 0

    for i in range(len(txt)-1):
        if txt[i] in [".","?","!"] and txt[i-1] not in [".","?","!"]:
            count += 1
    return count


def count_words(txt:str):
    count = 0

    for i in range(len(txt)-1):
        if not txt[i].isalnum() and txt[i-1].isalnum():
            count += 1
    return count


def count_letters(txt:str):
    count = 0

    for i in range(len(txt)-1):
        if txt[i].isalnum():
            count += 1
    return count


if __name__ == "__main__":
    main()
