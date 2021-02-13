# CS2513 - Assignment 1
# Jack O'Connor - 119319446

class Character:

    """
    For all Character classes (and subclasses), when initialising any instance of the class with parameter values of the incorrect
    type, type ERROR will be printed for each incorrect parameter. The class will still be instantiated due to no errors being raised.
    Due to this, if a Character is initialized with an incorrect attribute, that attribute will be missing from that instance of
    the class. Any methods that use this attribute will raise an AttributeError, such as attempting to print the Character.
    I thought about having all attributes default to None before initialisation but decided against this as it is not specified and
    would still lead to issues down the line in greater than and fight checks.

    If an attempt to set an incorrectly typed attribute to an already instantiated character object is made, it will retain its previous value.
    """

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def __str__(self):
        return f"{self.name} {self.strength}"

    def __gt__(self, other):
        if isinstance(other, Character):
            return self.strength > other.strength
        else:
            print("type ERROR")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("type ERROR")

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        # Need boolean check also since isinstance(True/False, int) is True.
        if isinstance(strength, bool) or (not isinstance(strength, int) and not isinstance(strength, float)):
            print("type ERROR")
        else:
            if strength < 0:
                strength = 0
            elif strength > 5:
                strength = 5
            self.__strength = float(strength)

    def fight(self, other):
        # If other is not a Character class, other's > operation won't support Character objects.
        if not isinstance(other, Character):
            print("type ERROR")
        elif self > other:
            self.strength = self.strength + 1.0
            print(self)
        elif other > self:
            other.strength = other.strength + 1.0
            print(other)
        else:
            self.strength = self.strength - 0.5
            other.strength = other.strength - 0.5


class Orc(Character):

    """
    No need for any adjustments to Character fight method once Orc's __gt__ method is changed.
    """

    def __init__(self, name, strength, weapon):
        super().__init__(name, strength)
        self.weapon = weapon

    def __str__(self):
        return f"{super().__str__()} {self.weapon}"

    def __gt__(self, other):
        if isinstance(other, Orc):
            if self.weapon and not other.weapon:
                return True
            elif not self.weapon and other.weapon:
                return False
            else:
                return super().__gt__(other)
        elif isinstance(other, Character):
            if not self.weapon:
                return False
            else:
                return super().__gt__(other)
        else:
            print("type ERROR")  # Other isn't Orc or Human.

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, weapon):
        if isinstance(weapon, bool):
            self.__weapon = weapon
        else:
            print("type ERROR")


class Human(Character):
    def __init__(self, name, strength, kingdom):
        super().__init__(name, strength)
        self.kingdom = kingdom

    def __str__(self):
        return f"{super().__str__()} {self.kingdom}"

    def __gt__(self, other):
        if isinstance(other, Orc):
            if other.weapon:
                return super().__gt__(other)
            else:
                return True  # No weapon means orc loses by default.
        elif isinstance(other, Character):
            return super().__gt__(other)
        else:
            print("type ERROR")

    @property
    def kingdom(self):
        return self.__kingdom

    @kingdom.setter
    def kingdom(self, kingdom):
        if isinstance(kingdom, str):
            self.__kingdom = kingdom
        else:
            print("type ERROR")

    def fight(self, other):
        if isinstance(other, Human):
            print("fight ERROR")
        else:
            super().fight(other)


class Archer(Human):
    def __init__(self, name, strength, kingdom):
        super().__init__(name, strength, kingdom)


class Knight(Human):

    """
    archers_list maintains it's current value in the case of an attempt to set
    archers_list to an invalid value.
    """

    def __init__(self, name, strength, kingdom, archers_list):
        super().__init__(name, strength, kingdom)
        self.archers_list = archers_list

    def __str__(self):
        temp = ""
        for x in self.archers_list:
            temp += x.__str__() + ', '
        temp = temp[:-2]
        return f"{super().__str__()} [{temp}]"

    @property
    def archers_list(self):
        return self.__archers_list

    @archers_list.setter
    def archers_list(self, archers_list):
        temp = []
        flag = True  # Set to false if there is a non-archer in archer list.
        for x in archers_list:
            if isinstance(x, Archer):
                if x.kingdom == self.kingdom:
                    temp.append(x)
            else:
                flag = False
                print("archers list ERROR")
                break
        if flag:
            self.__archers_list = temp
