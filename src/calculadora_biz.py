class CalculadoraBiz:

    def action(self, **kwargs):
        act = {
            "x": self._mult,
            "/": self._div,
            "+": self._sum,
            '-': self._sub
        }
        func = act.get(kwargs["action"], lambda: "Invalid action")
        return func(kwargs["a"], kwargs["b"])
    
    def _mult(self, a, b):
        return a * b

    def _div(self, a, b):
        return a / b

    def _sum(self, a, b):
        return a + b

    def _sub(self, a, b):
        return a - b