print("0 в качестве знака операции"
      "\nзавершит работу программы\n")

while True:
    s = input("Знак (+, -, *, /): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print("%.2f" % (a + b))
        elif s == '-':
            print("%.2f" % (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

# Тесты
import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['+', '1', '2', '0'])
    def test_addition(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertIn('3.00', output.getvalue())

    @patch('builtins.input', side_effect=['-', '1', '2', '0'])
    def test_subtraction(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertIn('-1.00', output.getvalue())

    @patch('builtins.input', side_effect=['*', '2', '2', '0'])
    def test_multiplication(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertIn('4.00', output.getvalue())

    @patch('builtins.input', side_effect=['/', '1', '2', '0'])
    def test_division(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertIn('0.50', output.getvalue())

    @patch('builtins.input', side_effect=['+', str(sys.float_info.min), str(sys.float_info.max), '0'])
    def test_addition_min_max(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertIn(str(sys.float_info.min + sys.float_info.max), output.getvalue())

    @patch('builtins.input', side_effect=['-', str(sys.float_info.max), str(sys.float_info.min), '0'])
    def test_subtraction_min_max(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertIn(str(sys.float_info.max - sys.float_info.min), output.getvalue())

    @patch('builtins.input', side_effect=['*', str(sys.float_info.min), str(sys.float_info.min), '0'])
    def test_multiplication_min_max(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertNotIn(str(sys.float_info.min / sys.float_info.min), output.getvalue())

    @patch('builtins.input', side_effect=['/', str(sys.float_info.max), str(sys.float_info.min), '0'])
    def test_division_min_max(self, input):
        with patch('sys.stdout', new=StringIO()) as output:
            calculator()
        self.assertIn(str(sys.float_info.max / sys.float_info.min), output.getvalue())

if __name__ == '__main__':
    unittest.main()
