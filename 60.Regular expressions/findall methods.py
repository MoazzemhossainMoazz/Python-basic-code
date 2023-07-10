import re
pattern = r"color"
print(re.findall(pattern,"Green is a color, Grass color is green"))
pattern2 = r"col"
print(re.findall(pattern2,"Green is color, Grass color is green"))
pattern3 = r"Green"
print(re.findall(pattern3,"Green is a color, Grass color is green"))
