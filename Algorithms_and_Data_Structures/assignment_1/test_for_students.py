# ------------------------------------------------
# Object Oriented Programming - Inheritance
# ------------------------------------------------
# Notes for the students:
# This is just a subset of the testing that I am running myself for evaluating the assignments.
# In your testing, you have to implement much more tests than these ones ;)
# Here I am implementing unit test (you still do not know what they are and this is ok, you will learn it in this degree)
# This code is just meant to test your code, but you do not need to understand the unit test at this stage.
# When you run this module, if the test is correct, you will get an ok and FAIL otherwise
# Before running this test, you must change YOUR_MODULE_NAME by the name of your module.


from OConnor_Jack import *

import unittest
import io
import sys
from contextlib import contextmanager
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err



class charactersTest(unittest.TestCase):

    # ------------------------------------------------
    #   Classes' constructor check
    # ------------------------------------------------


    def test_values_range_constructor_Archer(self):
        # Archers' check
        archer=Archer("archer1", 5.3, "Gondor")
        assert archer.strength == 5.0  # test : the result should be: 5
        pass

    def test_values_types_constructor_Orc(self):
        # Orcs' check
        with captured_output() as (out, err): Orc(1,4.3, False)
        output = out.getvalue().strip()
        assert (output == "type ERROR" or output == "type Error")  # test : the result should be: print("type Error")
        pass


    # ------------------------------------------------
    #   Properties check
    # ------------------------------------------------
    def test_properties_access_check_Orc(self):
        orc=Orc("Ogrorg", 4.1, True)
        assert orc.name == "Ogrorg"  # test  : properties for getting values
        assert orc.strength == 4.1   # test : properties for getting values
        assert orc.weapon == True    # test : properties for getting values
        orc.name = "Grunch"
        assert orc.name == "Grunch"  # test : properties for setting values
        orc.strength = 3.2
        assert orc.strength == 3.2   # test : properties for setting values
        orc.weapon = False
        assert orc.weapon == False   # test : properties for setting values


    # ------------------------------------------------
    #   Functionalities check
    # ------------------------------------------------

    def test_functionalities_str_Orc(self):
      pass

    def test_functionalities_str_Archer(self):
        a1=Archer("archer1", 3.3, "Gondor")
        with captured_output() as (out, err):  print(a1)
        output = out.getvalue().strip()
        assert (output == "archer1 3.3 Gondor")


    def test_functionalities_greater_Orc(self):
        orc1=Orc("Ogrorg", 3.3, True)
        orc2=Orc("Grunch",4.9, False)
        assert (orc1>orc2) == True   # test : > check - the result should be: True
        pass


    def test_functionalities_fight_truncation_Archer_Knight_Orc(self):
        a2=Archer("archer2", 2.3, "Pepe")
        k1= Knight("Aragorn", 5, "Gondor",[])
        orc1=Orc("Ogrorg", 5, True)
        a2.fight(orc1)
        assert orc1.strength==5 and a2.strength==2.3
        pass


    # ------------------------------------------------
    #   Inheritance check
    # ------------------------------------------------



if __name__ == '__main__':

    unittest.main(verbosity=2)
