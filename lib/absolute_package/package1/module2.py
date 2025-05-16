# Tests if module2 uses absolute imports correctly
from package1.subpackage2.module2 import function1

def test_module2_absolute_import():
    assert function1() == "Function 1 from module1"