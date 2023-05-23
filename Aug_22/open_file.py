"""myfile = open("fruits.txt")
content = myfile.read()
myfile.close()"""


"""read file"""
"""with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)"""

"""write to a file"""

"""with open("vege.txt", "w") as myfile:
    myfile.write("tomato\nCucumner\nOnion")"""

"""append to a file"""

with open("vege.txt", "a+") as myfile:
    myfile.write("\nokra")
    myfile.seek(0)
    content = myfile.read()

print(content)