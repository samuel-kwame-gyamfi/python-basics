# Mad Libs project

# Step 1: Collect input from the user
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")

# Step 2: Use conditional logic to create different story paths
if noun1.lower() == "lion" or verb1.lower() == "roar":
    print("""
    In a small village, there was a LION who loved to ROAR every morning. 
    One day, it saw a RABBIT near the river, trying to JUMP. 
    They decided to work together and accomplished something amazing!
    """)
elif noun2.lower() == "cat" or verb2.lower() == "dance":
    print("""
    One day, a CAT decided to DANCE in the middle of the park. 
    While doing so, it met a DOG that wanted to SING together. 
    They both became best friends and spent the whole day having fun!
    """)
else:
    print("There's no story for these choices.")



