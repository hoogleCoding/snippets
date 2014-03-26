import unittest

from injector import Requirement, Inject

class ClassA(object):
    pass

class ClassC(object):
    pass

@Requirement(ClassC)
class ClassB(object):
    def __init__(self, classC):
        self.classC = classC

@Inject()
class TypedClassB(object):
    def __init__(self, classC:ClassC):
        self.classC = classC

@Requirement(ClassB)
@Requirement(ClassA)
class PatchMe(object):
    def __init__(self, classA, classB):
        self.classA = classA
        self.classB = classB

@Inject()
class TypedPatchMe(object):
    def __init__(self, classA:ClassA, classB:TypedClassB):
        self.classA = classA
        self.classB = classB

class TestSingleInjector(unittest.TestCase):
    def test_it_should_inject_specified_class_hierarchies(self):
        patched = PatchMe()
        self.assertIsInstance(patched.classB.classC, ClassC)

    def test_it_should_inject_class_hierarchies_based_on_type(self):
        patched = TypedPatchMe()
        self.assertIsInstance(patched.classB.classC, ClassC)


if __name__=="__main__":
    unittest.main()
