"""
f = open("welcome.txt", "r")
print(f.read())
f.close()

"""
f = open("welcome.txt", "a")
f.write("Now the file has more content!" + "\n")
f.close()


f = open("welcome.txt", "r")
print(f.read())
f.close()

