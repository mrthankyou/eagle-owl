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

# Retrieves the blocks for the if/else instructions
def get_if_else_instructions(if_inst):
  if if_inst.is_if():
    first_true_inst = if_inst.first_true_instruction()
    first_false_inst = if_inst.first_false_instruction()
    return [first_true_inst, first_false_inst]
  else:
    return [if_inst]

# Finds a call in a given instruction
def find_call_in_instruction(inst: Instruction, call_name: str):
  calls = inst.get_callee_values()
  found_call = None
  for call in calls:
    if call.name == call_name:
      found_call = call 
      break

  return found_call

# Checks if a function is a new variable
def is_new_var_instruction(inst: Instruction):
  return inst.procedure_graph_node.to_json()['type'] == "NodeType.VARIABLE"

# Borrowed from utils.py since this function is required.
def is_none(obj):
    return obj == None or isinstance(obj, NoneObject)