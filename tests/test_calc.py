from src.calculadora_biz import CalculadoraBiz
import unittest

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc_biz = CalculadoraBiz()

    def test_action_mult(self):
        args = {"action": "x", "a": 1, "b": 2 }
        out = self.calc_biz.action(**args)
        self.assertEqual(out, 2)
    
    def test_action_div(self):
        args = {"action": "/", "a": 1, "b": 2 }
        out = self.calc_biz.action(**args)
        self.assertEqual(out, 0.5)

    def test_action_sum(self):
        args = {"action": "+", "a": 1, "b": 2 }
        out = self.calc_biz.action(**args)
        self.assertEqual(out, 3)

    def test_action_sub(self):
        args = {"action": "-", "a": 1, "b": 2 }
        out = self.calc_biz.action(**args)
        self.assertEqual(out, -1)

    def test_mult(self):
        out = self.calc_biz._mult(3, 6)
        self.assertEqual(out, 18)
    
    def test_div(self):
        out = self.calc_biz._div(3, 6)
        self.assertEqual(out, 0.5)

    def test_sum(self):
        out = self.calc_biz._sum(3, 6)
        self.assertEqual(out, 9)

    def test_sub(self):
        out = self.calc_biz._sub(3, 6)
        self.assertEqual(out, -3)
