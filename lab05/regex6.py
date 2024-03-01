import re

pattern = re.compile(r'[ ,.]')

with open('row.txt', 'r') as file:
    for line in file:
        modified_line = pattern.sub(':', line)
        print(modified_line.strip())
