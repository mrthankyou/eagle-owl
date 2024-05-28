# Description: Extends functionality for state variable related queries

def get_state_variable_write_instructions(state_var):
  sv_write_instructions = []  

  if state_var.is_immutable() or state_var.is_constant():
    return sv_write_instructions
  
  ## TODO: we should also scan base and derived contracts (assuming for base contracts the current contract doesn't include inherited functions)
  contract = state_var.contract()
  if is_none(contract):
    return sv_write_instructions

  for func in contract.functions().exec():
    for inst in func.instructions().exec():
      if inst.is_storage_write():
          for dest in inst.get_dest():
              if dest.expression == state_var.name:
                  sv_write_instructions.append(inst)

  
  return sv_write_instructions

## Borrowed from utils.py
def is_none(obj):
  return obj == None or isinstance(obj, NoneObject)
