#TODO: Create a letter using starting_letter.txt 
#Save the letters in the folder "ReadyToSend".
def ready_to_send(name,letter):
    file = open(f"Output\\ReadyToSend\\Letter_for_{name}.txt","w")
    file.write(letter)
    file.close()


#for each name in invited_names.txt
with open("Input\Letters\starting_letter.txt") as file:
    letter = file.read()

with open(r"Input\Names\invited_names.txt","r") as file:
    name = file.read()

names = name.split("\n")

for name in names:
    change = letter
    send = change.replace("[name]",name)
    ready_to_send(name,send)    

#Replace the [name] placeholder with the actual name.
