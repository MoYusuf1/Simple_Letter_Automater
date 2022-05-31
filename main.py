# TODO: Create a letter using starting_letter.txt
# TODO: Each name in invited_names.txt
# TODO: Replace the [name] placeholder with the actual name.
# TODO: Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)
