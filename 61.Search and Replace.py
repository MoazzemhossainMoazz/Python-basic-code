import re
pattern = r"color"
text1 = "Green is a color, Grass color is green"
text2 = re.sub(pattern,"Color",text1)
text3 = re.sub(pattern,"Color",text1, count=1)
print(text2)
print(text3)