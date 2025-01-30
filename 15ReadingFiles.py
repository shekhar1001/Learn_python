from sys import argv
script, shekhar=argv
txt = open(shekhar)
print(f"Here's your file {shekhar}:")
print(txt.read())
print("Type the shekhar again:")
file_again=input("> ")

txt_again=open(file_again)

print(txt_again.read())