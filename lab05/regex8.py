import re
text = "TextForExample"
def splitUp(s):
    return re.findall(r"[A-Z][a-z]+", text)

print(splitUp(text))