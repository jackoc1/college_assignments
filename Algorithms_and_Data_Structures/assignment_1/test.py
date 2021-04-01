# CS2513 - Assignment 1
# Jack O'Connor - 119319446

from OConnor_Jack import Orc


# ORC v ORC TESTS
test_orc = Orc("Ngba", 3.0, True)

# Instantiation tests
print("INSTANTIATION TESTS\n")

# Valid instantiation
try:
    test_orc = Orc("Ngba", 3.0, True)
    print("Instantiation test 1: Success")
except:
    print("Instantiation test 1: Error caught")

# Invalid instantiation
try:
    test_orc = Orc(800, "strength", "weapon")
    print("Instantiation test 2: Success")
except:
    print("Instantiation test 2: Error caught")


# __str__ tests
print("\nTO STRING TESTS\n")

test_orc = Orc("Ngba", 3.0, True)
try:
    print(test_orc)
except:
    print("To string test: Error caught")


# Name getter and setter tests
print("\nNAME GETTER AND SETTER TESTS\n")

# Valid assignment
test_orc = Orc("Ngba", 3.0, True)
try:
    print("Name before reassignment", test_orc.name)
    test_orc.name = "Lorenz"
    print("Name after reassignment", test_orc.name)
except:
    print("Name test 1: Error caught")

# Invalid assignment
test_orc = Orc("Ngba", 3.0, True)
try:
    print("Name before reassignment", test_orc.name)
    test_orc.name = False
    print("Name after reassignment", test_orc.name)
except:
    print("Name test 2: Error caught")


# Strength getter and setter tests
print("\nSTRENGTH GETTER AND SETTER TESTS\n")

# Valid assignment
test_orc = Orc("Ngba", 3.0, True)
try:
    print("Strength before reassignment", test_orc.strength)
    test_orc.strength = 2.3
    print("Strength after reassignment", test_orc.strength)
except:
    print("Strength test 1: Error caught")

# Invalid assignment
test_orc = Orc("Ngba", 3.0, True)
try:
    print("Strength before reassignment", test_orc.strength)
    test_orc.strength = False
    print("Strength after reassignment", test_orc.strength)
except:
    print("Strength test 2: Error caught")

# Valid assignment, but outside domain [0, 5]
test_orc = Orc("Ngba", 3.0, True)
try:
    print("Strength before reassignment", test_orc.strength)
    test_orc.strength = -10
    print("Strength after reassignment", test_orc.strength)
except:
    print("Strength test 3: Error caught")


# Weapon getter and setter tests
print("\nWEAPON GETTER AND SETTER TESTS\n")

# Valid assignment
test_orc = Orc("Ngba", 3.0, True)
try:
    print("Weapon before reassignment", test_orc.weapon)
    test_orc.weapon = False
    print("Weapon after reassignment", test_orc.weapon)
except:
    print("Weapon test 1: Error caught")

# Invalid assignment
test_orc = Orc("Ngba", 3.0, True)
try:
    print("Weapon before reassignment", test_orc.weapon)
    test_orc.weapon = "False"
    print("Weapon after reassignment", test_orc.weapon)
except:
    print("Weapon test 2: Error caught")


# > tests
print("\n'>' TESTS\n")

# test_orc > test_orc 2
test_orc = Orc("Ngba", 3.0, True)
test_orc2 = Orc("Ricardo", 2.8, True)
try:
    print(test_orc > test_orc2)
except:
    print("'>' test 1: Error caught")

# test_orc == test_orc2
test_orc = Orc("Ngba", 3.0, True)
test_orc2 = Orc("Ricardo", 3.0, True)
try:
    print(test_orc > test_orc2)
except:
    print("'>' test 2: Error caught")

# test_orc < test_orc2
test_orc = Orc("Ngba", 3.0, True)
test_orc2 = Orc("Ricardo", 3.2, True)
try:
    print(test_orc > test_orc2)
except:
    print("'>' test 3: Error caught")

# test_orc2 doesn't have weapon
test_orc = Orc("Ngba", 3.0, True)
test_orc2 = Orc("Ricardo", 5.0, False)
try:
    print(test_orc > test_orc2)
except:
    print("'>' test 4: Error caught")


# Fight tests
print("\nFIGHT TESTS\n")

# test_orc wins
test_orc = Orc("Ngba", 3.0, True)
test_orc2 = Orc("Ricardo", 2.8, True)
try:
    test_orc.fight(test_orc2)
except:
    print("Fight test 1: Error caught")

# test_orc ties
test_orc = Orc("Ngba", 3.0, True)
test_orc2 = Orc("Ricardo", 3.0, True)
try:
    test_orc.fight(test_orc2)
except:
    print("Fight test 2: Error caught")

# test_orc loses
test_orc = Orc("Ngba", 3.0, True)
test_orc2 = Orc("Ricardo", 3.2, True)
try:
    test_orc.fight(test_orc2)
except:
    print("Fight test 3: Error caught")

# test_orc wins with max strength
test_orc = Orc("Ngba", 5.0, True)
test_orc2 = Orc("Ricardo", 3.2, True)
try:
    test_orc.fight(test_orc2)
except:
    print("Fight test 4: Error caught")

# tie with both having min strength
test_orc = Orc("Ngba", 0, True)
test_orc2 = Orc("Ricardo", 0, True)
try:
    test_orc.fight(test_orc2)
except:
    print("Fight test 5: Error caught")
