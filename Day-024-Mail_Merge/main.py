
PLACE_HOLDER = "[name]"

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    invited_name =  names.readlines()

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in invited_name:
        striped_name = name.strip()
        replaced_content = letter_content.replace(PLACE_HOLDER, striped_name)
        print(replaced_content)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_{striped_name}.txt" , mode = "w") as create_letter:
            create_letter.write(replaced_content)

