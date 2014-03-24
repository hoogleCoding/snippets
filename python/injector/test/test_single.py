import unittest

from requirement import Requirement

class ClassA(object):
    pass

@Requirement(ClassA)
class PatchMe(object):
    def __init__(self, classA):
        self.classA = classA

class TestSingleInjector(unittest.TestCase):
    def test_it_should_inject_a_single_class(self):
        patched = PatchMe()
        self.assertIsNotNone(patched)
        self.assertIsNotNone(patched.classA)


if __name__=="__main__":
    unittest.main()
