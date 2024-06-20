# Returns common subtraction functions
def math_subtraction_function_names():
  return [
    "safeSub",  # Custom func: safeSub(2,1)
    "sub",      # Safemath: 2.sub(1, "revert message") Can also be sub(2,1,"revert message")
    "subtract"  # Custom func: subtract(2, 1) 
  ]

# Returns common addition functions
def math_addition_function_names():
  return [
    "add",     # Safemath: add(uint256 a, uint256 b)
    "safeAdd", # Custom func: safeAdd(uint a, uint b)
  ]

# Returns common multiplication functions
def math_multiply_function_names():
  return [
    "mul",    # Safemath: mul(uint256 a, uint256 b)
    "safeMul" # Custom func: safeMul(uint a, uint b)
  ]

# Returns common division functions
def math_division_function_names():
  return [
    "div", # Safemath: div(uint256 a, uint256 b) or div(a, b, errorMessage)
  ]

# This function returns an array of symbolic math operations given an Instruction. This function recursively goes through all operations.
def get_all_symbolic_math_operations(operable, operand: str):
  def get_child_math_ops(ops, operand):
    math_ops = get_symbolic_math_ops(ops, operand)
    for op in ops:
        if isinstance(op, ValueExpression):
          children_ops = get_child_math_ops(op.get_operands(), operand)
          math_ops.extend(children_ops)
    return math_ops

  ops = operable.get_operands()
  return get_child_math_ops(ops, operand)
 
# This function returns an array of symbolic math operations given an array of operations.
def get_symbolic_math_ops(ops, operand):
  i = 0
  math_ops = []
  for op in ops:
    if op.expression == operand:
      left_hand_op = ops[i - 1]
      right_hand_op = ops[i + 1]
      math_ops.append([left_hand_op, right_hand_op])
    i = i + 1    
  return math_ops

def get_solidity_arithmetic_operators():
    return [
        "+",    # Addition
        "-",    # Subtraction
        "*",    # Multiplication
        "/",    # Division
        "%",    # Modulo
        "**",   # Exponentiation
        "+",    # Unary plus
        "-",    # Unary minus
        "&",    # Bitwise AND
        "|",    # Bitwise OR
        "^",    # Bitwise XOR
        "~",    # Bitwise NOT
        "<<",   # Shift left
        ">>"    # Shift right
    ]