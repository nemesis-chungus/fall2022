import os

sourceDir = os.path.dirname(__file__)

f = open(os.path.join(sourceDir, "week8-output.txt"))
lines = f.readlines()
words = (" ")
words = lines
for word in words:
    print({word.strip()})
if word.strip() != " ":
    print(f"words: {len(words)}")
f.close