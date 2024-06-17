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