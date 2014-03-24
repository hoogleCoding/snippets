"""
Defines a initialzation-time requirement for an object.
"""
class Requirement(object):
    def __init__(self, requirement):
        self.requirement = requirement

    def __call__(self, original_function):
        def f(*args):
            return original_function(self.requirement(),*args)
        return f

