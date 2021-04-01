from OConnor_Jack import *

# INITIALISATION AND STRING METHOD TESTS
orc = Orc("Ngba", 3, True)
archer = Archer("Leslie", 3, "Wales")
knight = Knight("Arthur", 4, "Wales", [archer])

print("(1) Initialisation and __str__() tests")
print(f"\tYour output: {orc} | {archer} | {knight}")
print(f"\tCorrect output: Ngba 3 True | Leslie 3 Wales | Arthur 4 Wales [Leslie 3 Wales]")
print()

# ORC SETTERS AND GETTERS WITH INCORRECT TYPES
print("(2) Orc getters and setters")
