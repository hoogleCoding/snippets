import unittest

from requirement import Requirement

class ClassA(object):
    pass

class ClassC(object):
    pass

@Requirement(ClassC)
class ClassB(object):
    def __init__(self, classC):
        self.classC = classC

@Requirement(ClassB)
@Requirement(ClassA)
class PatchMe(object):
    def __init__(self, classA, classB):
        self.classA = classA
        self.classB = classB

class TestSingleInjector(unittest.TestCase):
    def test_it_should_inject_class_hierarchies(self):
        patched = PatchMe()
        self.assertIsInstance(patched.classB.classC, ClassC)


if __name__=="__main__":
    unittest.main()
