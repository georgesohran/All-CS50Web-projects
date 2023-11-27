def main():

    text = str(input("Text: "))

    sentences = count_sentences(text)
    words = count_words(text)
    letters = count_letters(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    grade = int(round(0.0588 * L - 0.296 * S - 15.8))

#    print(f"{sentences}--{words}--{letters}\n{L}--{S}")
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


def count_sentences(txt:str):
    count = 0

    for i in range(len(txt)):
        if txt[i] in [".","?","!"] and txt[i-1] not in [".","?","!"]:
            count += 1
    return count


def count_words(txt:str):
    count = 0

    for i in range(len(txt)):
        if txt[i] in [".","?","!",",","/"," "] and txt[i-1].isalnum():
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
