import re

with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

book.count("Chapter")

pattern = re.compile("Chapter [0-9]")
re.findall(pattern, book)
