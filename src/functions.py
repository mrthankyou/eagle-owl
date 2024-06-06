# Checks if a function is a interface function
def is_interface_function(func: Function):
  return len(func.instructions().exec()) == 0
