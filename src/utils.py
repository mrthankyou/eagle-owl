# Description: Add utility functions for general queries

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

