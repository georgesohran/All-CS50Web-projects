def convert(em):
    em = em.replace(":)","🙂")
    em = em.replace(":(","☹️")
    return em

def main():
    face = input()
    print(convert(face))
main()