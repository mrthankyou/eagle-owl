# Returns common subtraction functions
def math_subtraction_function_names():
  return [
    "safeSub", # safeSub(2,1) // Custom made func
    "sub",      # 2.sub(1, "revert message") // SafeMath. Can also be sub(2,1,"revert message")
    "subtract"  # subtract(2, 1) // OZ
  ]