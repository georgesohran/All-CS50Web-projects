import validators

def main():
    mail = input("What's your email address? ")
    if validators.email(mail):
        print("Valid")
    else:
        print("Invalid")

main()