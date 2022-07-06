import operator

class Calculator(object):
   def parse(self, expression):
      values = expression.split()
      return self.compute_values(values)

   def compute_values(self, values):
      operations = { "+" : operator.add,
                     "-" : operator.sub,
                     "*" : operator.mul }
#                     "/" : operator.div }
      if len(values) == 1:
         return values[0]
      if values[0] in operations:
         if values[1] in operations:
               return BinaryExpression(operations[values[0]], self.compute_values(values[1:-1]), values[-1]).compute()
         return BinaryExpression(operations[values[0]], values[1], values[2]).compute()

      return BinaryExpression(values[0], values[1], values[2]).compute()


class BinaryExpression(object):
   def __init__(self, operations, left_expression, right_expression):
      self.operations = operations
      self.left_expression = int(left_expression)
      self.right_expression = int(right_expression)

   def compute(self):
      return self.operations(self.left_expression, self.right_expression)
