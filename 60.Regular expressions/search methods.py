import re
pattern = r"Color"
if re.search(pattern,"Green is a color, grass color is green"):
    print("Match")
else:
    print("Not matched")

print("\nAnother part: ")

if re.search(pattern, "Green is a Color, grass color is green"):
    print("Match")
else:
    print("Not match")