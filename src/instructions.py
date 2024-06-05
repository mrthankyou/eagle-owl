# Finds the root call in an instruction
def get_root_call(inst: Instruction):
  if len(inst.get_callee_values()) > 0:
    return inst.get_callee_values()[0]
  else:
    return None

# Finds the root variable of the instruction
def find_root_variable(inst: Instruction):
    def recursive_search(obj):
      None
      if is_none(obj):
          return None
      elif isinstance(obj, Var):
          print(obj.type)
          return obj
      elif isinstance(obj, Call):
          return recursive_search(obj.get_call_qualifier())
      else:
          return obj

    if not inst.is_call():
        return

    root_call = get_root_call(inst)
    recursive_search(root_call)

def get_if_else_instructions(if_inst):
  if if_inst.is_if():
    first_true_inst = if_inst.first_true_instruction()
    first_false_inst = if_inst.first_false_instruction()
    return [first_true_inst, first_false_inst]
  else:
    return [if_inst]

# Borrowed from utils.py since this function is required.
def is_none(obj):
    return obj == None or isinstance(obj, NoneObject)