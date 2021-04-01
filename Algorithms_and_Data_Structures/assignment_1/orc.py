# CS2513 - Assignment 1
# Jack O'Connor - 119319446

class Orc:
    def __init__(self, name, strength, weapon):
        # name
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name is not of type string")
        # strength
        strength = float(strength)  # will catch non_numeric inputs
        if 0 <= strength <= 5:
            self._strength = strength
        elif strength < 0:
            self._strength = 0
        else:
            self._strength = 5
        # weapon
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            raise ValueError("Weapon is not of type boolean")

    def __str__(self):
        print(self._name, self._strength, self._weapon) # should return

    def __gt__(self, other):
        if self._weapon and not other.weapon:
            return True
        elif self._weapon and other.weapon:
            return self._strength > other.strength
        else:
            return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Typerror("Name was not of type string.")

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        try:
            strength = float(strength)  # will catch non_numeric inputs
            if 0 <= strength <= 5:
                self._strength = strength
            elif strength < 0:
                self._strength = 0
            else:
                self._strength = 5
        except TypeError:
            print("Strength was not a numeric type.")

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            raise TypeError("Weapon was not of type boolean.")

    def fight(self, other):
        if self > other:
            self._strength = min(self._strength + 1, 5)
            self.__str__()
        elif other > self:
            other.strength = min(other.strength + 1, 5)
            other.__str__()
        else:
            self._strength = max(0, self._strength - 0.5)
            other.strength = max(0, other.strength - 0.5)
            print("Tie")
            self.__str__()
            other.__str__()
