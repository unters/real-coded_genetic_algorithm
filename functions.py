from Function import Function


class RosenbrockFunction(Function):
    """ Rosenbrock function.
    Global min at (x,y) = (1,1), where f(x,y) = 0. """
    def function(self, x, y):
        return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


class HimmelblauFunction(Function):
    """ Himmelblau function.
    Local min at (x,y) ~= (-0.270845,-0.923039), where f(x,y) ~= 181.617
    Global min f(x,y) = 0 at (x,y) = (3,2),
                                     (-2.805,3.131),
                                     (-3.779,-3.283),
                                     (3.584,-1.848). """
    def function(self, x, y):
        return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


class SphereFunction(Function):
    """ Sphere function.
    Global min at (x,y) = (0,0), f(x,y) = 0. """
    def function(self, x, y):
        return x ** 2 + y ** 2
