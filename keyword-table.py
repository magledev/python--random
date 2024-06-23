# Print a table of Python's reserved keywords
import keyword
import os

keywords = keyword.kwlist
columns = 4
rows = (len(keywords) + columns - 1) // columns
dmarc = ("-" * 80)

os.system('clear')

# Table header
print(dmarc + "\nPython Reserved Keywords\n" + dmarc)

# Print keywords
for i in range(rows):
    for j in range(columns):
        index = i + j * rows
        if index < len(keywords):
            print(f"{keywords[index]:<20}", end="")
    print()

# Print footer
print(dmarc)
