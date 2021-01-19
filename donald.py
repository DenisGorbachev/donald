from z3 import *

# donald + gerald = robert

donald = "donald"
gerald = "gerald"
robert = "robert"
names = [donald, gerald, robert]
digits = dict()
solver = Solver()

for name in names:
    for character in name:
        if character not in digits:
            digit = Int(character)
            solver.add(digit >= 0)
            solver.add(digit <= 9)
            digits[character] = digit


def num(name):
    return Sum([digits[name[len(name) - index - 1]] * pow(10, index) for index in range(0, len(name))])


solver.add(Distinct(*digits.values()))
solver.add(num("donald") + num("gerald") == num("robert"))

print(solver.assertions())
print("Solving, please wait...")
print(solver.check())
print(solver.model())
