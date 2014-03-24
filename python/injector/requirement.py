#!/usr/bin/env python

class Requirement(object):
    def __init__(self, requirement):
        self.requirement = requirement

    def __call__(self, original_function):
        def f(*args):
            return original_function(self.requirement(),*args)
        return f

class ClassA(object):
    def __init__(self):
        print("ClassA init called")

    def speak(self):
        print("ClassA speaking")

class ClassB(object):
    def __init__(self):
        print("ClassB init called")

    def speak(self):
        print("ClassB speaking")

@Requirement(ClassB)
@Requirement(ClassA)
class PatchMe(object):
    def __init__(self, classA, classB, text):
        self.classA = classA
        self.classB = classB
        self.text = text

    def speak(self):
        print("PatchMe saying {}".format(self.text))
        self.classA.speak()
        self.classB.speak()

def main():
    patch = PatchMe("hello world")
    patch.speak()


if __name__ == "__main__":
    main()
