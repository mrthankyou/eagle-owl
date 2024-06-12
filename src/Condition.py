# This pull any conditional statements within an array of operands.
def get_conditional_statements(ops, expected_value_a, operand, expected_value_b):
  results = []
  for index in range(len(ops)):
    op = ops[index]

    if op.expression not in operand:
      continue

    value_a = ops[index - 1]
    value_a_expression = value_a.expression

    value_b = ops[index + 1]
    value_b_expression = value_b.expression


    if value_a_expression != expected_value_a and value_b_expression != expected_value_a:
      continue 

    if value_a_expression != expected_value_b and value_b_expression != expected_value_b:
      continue
 
    results.append([value_a, op, value_b])
  return results
