# Checks if a function is a interface function
def is_interface_function(func):
  return len(func.instructions().exec()) == 0
