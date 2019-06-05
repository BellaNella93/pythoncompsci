name="peanut butter jelly cups"
day= "Thursday, May 30th"
message1 = f"My name is {name} and today is {day}."
message2 ="This is the 2nd line."
message3= "This is the 3rd and final line." #new
messages = [message1, message2, message3] #new


filename = "nella\sunny.txt" #new
file = open (filename,"w")  # w stands for write
file.writelines(messages)
file.close()

with open(filename, 'w') as f: 
    for m in messages:
        f.write(f"{m}\n")  # in the f string each message will have a new line "/n"write new line
