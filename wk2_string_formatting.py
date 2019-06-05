#week2 string formatting
message = "hello world"
name = "Ornella"
# the old way, using "positional formatting"
print("%s is my message, %s is my name." %(message, name))

#the new way, using f-strings (formatted strings)
print (f"{message} is my message, {name} is my name.")
