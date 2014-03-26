"""
Defines a initialzation-time requirement for an object.
"""
class Requirement(object):
    def __init__(self, requirement):
        self.requirement = requirement

    def __call__(self, original_function):
        def f(*args, **kwargs):
            return original_function(self.requirement(),*args, **kwargs)
        return f

class Inject(object):
    def __call__(self, original_function):
        injects = original_function.__init__.__annotations__
        def f(*args, **kwargs):
            for inject in injects.keys():
                kwargs[inject] = injects[inject]()
            return original_function(*args, **kwargs)
        return f

