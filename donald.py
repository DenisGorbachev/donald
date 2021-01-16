from z3 import *

# donald + gerald = robert

donald = "donald"
gerald = "gerald"
robert = "robert"
names = [donald, gerald, robert]
digits = dict()
s = Solver()

for name in names:
    for character in name:
        if character not in digits:
            digit = Int(character)
            s.add(digit >= 0)
            s.add(digit <= 9)
            digits[character] = digit


def num(name):
    return Sum([digits[name[len(name) - index - 1]] * pow(10, index) for index in range(0, len(name))])


s.add(Distinct(*digits.values()))
s.add(num("donald") + num("gerald") == num("robert"))

print(s.assertions())
print("Solving, please wait...")
print(s.check())
print(s.model())
