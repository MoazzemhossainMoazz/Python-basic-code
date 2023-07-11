import re
pattern = r"^colo..r$" #1st 4 letter it will be 'colo' and last letter will be 'r'

if re.match(pattern,"colobar"):
    print("Matched.")


print("2nd way: ")
pattern = r"a*" # * means 0 or more

if re.match(pattern,"abcolor"):
    print("Matched")


print("3rd way: ")
pattern = r"(ab)*"

if re.match(pattern,"abcolor"):
    print("Match")


print("4th way: ")
pattern = r"a+" # + means 1 or more

if re.match(pattern,"color"):
    print("Matched")
else:
    print("not matched")


print("5th way: ")
pattern = r"a+"

if re.match(pattern,"acolor"):
    print("Matched")
else:
    print("Not matched")


print("6th way: ")
pattern = r"a+b"

if re.match(pattern,"abcolor"):
    print("Matched")
else:
    print("Not matched")


print("7th way: ")
pattern = r"a+b"

if re.match(pattern,"acolor"):
    print("Matched")
else:
    print("Not matched")


print("8th way: ")
pattern = r"a*b"

if re.match(pattern, "abcolor"):
    print("Match")
else:
    print("Not mathced")


print("9th way: ")
pattern = r"a*b"

if re.match(pattern, "bcolor"):
    print("Match")
else:
    print("Not mathced")



print("10th way: ")
pattern = r"a*b"

if re.match(pattern, "color"):
    print("Match")
else:
    print("Not mathced")



print("11th way: ")
pattern = r"ab(-)color"

if re.match(pattern, "ab-color"):
    print("Match")
else:
    print("Not mathced")



print("12th way: ")
pattern = r"ab(-)color"

if re.match(pattern, "abcolor"):
    print("Match")
else:
    print("Not mathced")


print("13th way: ")
pattern = r"ab(-)?color"

if re.match(pattern, "ab-color"):
    print("Match")
else:
    print("Not mathced")


print("14th way: ")
pattern = r"ab(-)?color"

if re.match(pattern, "abcolor"):
    print("Match")
else:
    print("Not mathced")

print("15th way: ")
pattern = r"a{1,3}$" #a{1,3}$ means a letter will have 1 to 3 times

if re.match(pattern, "a"):
    print("Match")
else:
    print("Not mathced")

if re.match(pattern, "aa"):
    print("Match")
else:
    print("Not mathced")

if re.match(pattern, "aaa"):
    print("Match")
else:
    print("Not mathced")

if re.match(pattern, "aaaa"):
    print("Match")
else:
    print("Not mathced")