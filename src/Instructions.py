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

def find_asserts(instructions):
  results = []

  for inst in instructions:
    for call in inst.get_callee_values():
      if call.name == "assert":
        results.append(inst)
        break

  return results

def has_asserts(instructions):
  return len(find_asserts(instructions)) > 0
