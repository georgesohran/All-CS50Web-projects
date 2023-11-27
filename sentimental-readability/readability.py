def main():

    text = str(input("Text: "))

    sentances = count_sentances(text)
    words = count_words(text)
    letters = count_letters(text)

    print(f"{sentances}--{words}--{letters}")

    L = 0
    S = 0

    grade = 0.0588 * L - 0.296 * S - 15.8


def count_sentances(txt:str):
    count = 0

    for i in range(len(txt)):
        if txt[i] in [".","?","!"] and txt[i-1] not in [".","?","!"]:
            count += 1
    return count


def count_words(txt:str):
    count = 0

    for i in range(len(txt)):
        if not txt[i].isalnum() and txt[i-1].isalnum():
            count += 1
    return count


def count_letters(txt:str):
    count = 0

    for i in range(len(txt)):
        if txt[i].isalnum():
            count += 1
    return count


if __name__ == "__main__":
    main()
