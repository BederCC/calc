#BederCasa
#coding:utf-8
import unittest
from calculator import Calculator

class TestCalculadora(unittest.TestCase):
   def test_add_three_four(self):
      self.aider(7, "+ 3 4")

#    def test_add_nine_two(self):
#       self.aider(11, "+ 9 2")

#    def test_add_twenty_two(self):
#       self.aider(22, "+ 20 2")

   def test_substract_four_three(self):
      self.aider(1, "- 4 3")

#    def test_substract_four_minus_three(self):
#       self.aider(100, "- 99 -1")

#    def test_multiply_four_three(self):
#       self.aider(12, "* 4 3")

#    def test_multiply_minus_four_thirtytwo(self):
#       self.aider(-128, "* -4 32")

#    def test_divide_four_three(self):
#       self.aider(1, "/ 4 3")

#    def test_divide_twelve_three(self):
#       self.aider(4, "/ 12 3")

#    def test_divide_minus_twelve_three(self):
#       self.aider(-4, "/ -12 3")

#    def test_add_add_four_three_four(self):
#       self.aider(11, "+ + 4 3 4")

#    def test_add_substract_four_three_four(self):
#       self.aider(5, "+ - 4 3 4")

#    def test_divide_multiply_three_four_four(self):
#       self.aider(3, "/ * 3 4 4")

#    def test_divide_add_four_four_four(self):
#       self.aider(2, "/ + 4 4 4")

#    def test_add_add_add_four_three_four_three(self):
#       self.aider(14, "+ + + 4 3 4 3")

#    def test_add_substract_substract_four_three_four_three(self):
#       self.aider(0, "+ - - 4 3 4 3")

#    def test_divide_multiply_multiply_two_two_two_eight(self):
#       self.aider(1, "/ * * 2 2 2 8")

# def test_add_add_add_add_four_three_four_three_four(self):
#    self.aider(18, "+ + + + 4 3 4 3 4")

# def test_divide_multiply_multiply_multiply_two_two_two_two_sixteen(self):
#    self.aider(1, "/ * * * 2 2 2 2 16")

# def test_add_add_three_four_substract_four_three(self):
#    self.aider(8, "+ + 3 4 - 4 3")

   def aider(self, expected, expression):
      calc = Calculator()
      actual = calc.parse(expression)
      self.assertEqual(expected, actual)

def run_tests():
   #Método para iniciar la sesión de testeo
   suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)
   unittest.TextTestRunner(verbosity=2).run(suite)

#corremos los tests sólo si fuimos llamados desde la consola
if __name__ == "__main__":
   run_tests()
