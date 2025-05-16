# Tests if module2 correctly imports from a sibling/parent module
from package2.subpackage1.subpackage2.module2 import function3

def test_relative_import():
    assert function3() == "Function 1 from module3"