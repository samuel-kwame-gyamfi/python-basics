#prompting the user for a vowel

alpha = input("Enter an alphabet: ").lower()

#match case statement

match alpha:
    case vowel if alpha in ["a", "e", "i", "o", "u"]:
        print(f"{alpha} is a vowel")
    case _:
        print(f"{alpha} is a consonant")
