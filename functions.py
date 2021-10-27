from Function import Function


class RosenbrockFunction(Function):
    """ Global min at (x,y) = (1,1), where f(x,y) = 0 """
    def function(self, x, y):
        return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

    def draw_plot(self):
        super(RosenbrockFunction, self).draw_plot([-2, 2], [-1, 3])


class HimmelblauFunction(Function):
    """ Local min at (x,y) ~= (-0.270845,-0.923039), where f(x,y) ~= 181.617
        Global min f(x,y) = 0 at (x,y) = (3.2),
                                         (-2.805,3.131),
                                         (-3.779,-3.283),
                                         (3.584,-1.848) """
    def function(self, x, y):
        return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

    def draw_plot(self):
        super(HimmelblauFunction, self).draw_plot([-4, 4], [-4, 4])


class SphereFunction(Function):
    """ TODO: Add description to SphereFunction. """
    def function(self, x, y):
        return x ** 2 + y ** 2

    def draw_plot(self):
        super(SphereFunction, self).draw_plot([-4, 4], [-4, 4])
