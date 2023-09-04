def flame(name1, name2):
    letters = ['F', 'L', 'A', 'M', 'E']

    # Remove common letters from the names.
    common_letters = set(name1).intersection(set(name2))
    for letter in common_letters:
        name1 = name1.replace(letter, '')
        name2 = name2.replace(letter, '')

    # Get the length of the remaining letters.
    length = len(name1) + len(name2)

    # Find the letter that corresponds to the length.
    index = length % len(letters)

    return letters[index]
name1= input("What is the first name?")
name2 = input("What is the second person's name?")
print(flame(name1, name2))
