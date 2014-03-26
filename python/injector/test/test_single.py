import unittest

from injector import Requirement, Inject

class ClassA(object):
    pass

@Requirement(ClassA)
class PatchMe(object):
    def __init__(self, classA):
        self.classA = classA

@Inject()
class TypedPatchMe(object):
    def __init__(self, classA:ClassA):
        self.classA = classA

class TestSingleInjector(unittest.TestCase):
    def test_it_should_inject_a_single_specified_class(self):
        patched = PatchMe()
        self.assertIsNotNone(patched)
        self.assertIsNotNone(patched.classA)

    def test_it_should_inject_a_single_class_depending_on_type(self):
        patched = TypedPatchMe()
        self.assertIsNotNone(patched)
        self.assertIsNotNone(patched.classA)
        self.assertIsInstance(patched.classA, ClassA)



if __name__=="__main__":
    unittest.main()
