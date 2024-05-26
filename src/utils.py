# Description: extends functionality to find use cases of msg.sender

from glider import *
def query():
  instructions = Instructions().exec(10000) 
  for instruction in instructions:
    if instruction_contains_direct_msg_sender_check(instruction):
      None
 
  return []

def is_none(obj):
  return obj == None or isinstance(obj, NoneObject)

def find_reverts(instructions):
  results = []

  for inst in instructions:
    for call in inst.get_callee_values():
      if call.name == "revert":
        results.append(inst)
        break

  return results

def has_reverts(instructions):
  return len(find_reverts(instructions)) > 0

def find_requires(instructions):
  results = []

  for inst in instructions:
    for call in inst.get_callee_values():
      if call.name == "require":
        results.append(inst)
        break

  return results

def has_requires(instructions):
  return len(find_requires(instructions)) > 0

def intra_instructions(function):
  None

