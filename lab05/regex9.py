import re
text = "TextForExample"
def splitUp(s):
    words = re.findall(r"[A-Z][a-z]+", s)
    return " ".join(words)
print(splitUp(text))