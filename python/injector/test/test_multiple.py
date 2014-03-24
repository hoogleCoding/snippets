import unittest

from requirement import Requirement

class ClassA(object):
    pass

class ClassB(object):
    pass

@Requirement(ClassB)
@Requirement(ClassA)
class PatchMe(object):
    def __init__(self, classA, classB):
        self.classA = classA
        self.classB = classB

class TestSingleInjector(unittest.TestCase):
    def test_it_should_inject_multiple_classes(self):
        patched = PatchMe()
        self.assertIsNotNone(patched)
        self.assertIsInstance(patched.classA, ClassA)
        self.assertIsInstance(patched.classB, ClassB)


if __name__=="__main__":
    unittest.main()
