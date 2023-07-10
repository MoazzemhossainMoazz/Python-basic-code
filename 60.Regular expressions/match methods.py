import re #re means regular expression
pattern = r"Color"
if re.match(pattern,"Green is a color, grass color is green"):
    print("Match")
else:
    print("Not match")


print("\n2nd part: ")

import re
pattern = r"Green"
if re.match(pattern,"Green is a color, grass color is green"):
    print("Match")
else:
    print("Not match")

print("\n3rd part: ")

pattern = r"col"
if re.match(pattern,"Green is a color, grass color is green"):
    print("Match")
else:
    print("Not match")

print("\n4th part: ")
pattern = r"color"
text = "Green is a color, grass color is green"
match = re.search(pattern,text)
if match:
    print(match.start()) #match 1st word and find out first point
    print(match.end()) #match 1st word and find out last point
    print(match.span()) #match 1st word and find out 1st letter and last letter point