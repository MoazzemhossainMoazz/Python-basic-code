import re
pattern = r"[aeiou]"

print("1st way: ")
if re.match(pattern,"aqweruiozcvzx"):
    print("Matched")
else:
    print("Not matched")

print("2nd way: ")
if re.match(pattern,"qwruzcvzxjkm"):
    print("Matched")
else:
    print("Not matched")

print("3rd way: ")
pattern = r"[A-J]"
if re.match(pattern,"Afasdfasdl"):
    print("Matched")
else:
    print("Not matched")

print("4th way: ")
pattern = r"[A-J]"
if re.match(pattern,"fasdfasdl"):
    print("Matched")
else:
    print("Not matched")

print("5th way: ")
pattern = r"[a-m]"
if re.match(pattern,"adfasdfm"):
    print("Matched")
else:
    print("Not matched")

print("6th way: ")
pattern = r"[a-m]"
if re.match(pattern,"nopqrst"):
    print("Matched")
else:
    print("Not matched")

print("7th way: ")
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"nopqrst"):
    print("Matched")
else:
    print("Not matched")

print("8th way: ")
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"noA6pqrst"):
    print("Matched")
else:
    print("Not matched")

print("8th way: ")
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"Aa7pqrst"):
    print("Matched")
else:
    print("Not matched")