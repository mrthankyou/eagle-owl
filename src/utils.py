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


def get_all_instructions(func):
  results = {}

  insts = func.instructions().exec()

  if len(insts) <= 1:
    return results

  # QUESTION: When querying for all instructions in a given function, is the first instruction always an EntryPoint instruction?
  if insts[0].is_entry_point():
    first_inst = insts[1]
  else:
    first_inst = insts[0]

  sig = first_inst.get_parent().signature()
  results[str(sig)] = [first_inst]

  # NOTE: This fails in a rare case hence why we have the try/except
  try:
    extended_next_instructions = first_inst.extended_next_instructions()
  except:
    return {}

  for inst in extended_next_instructions:
    if not inst.is_entry_point():
      sig = inst.get_parent().signature()
 
      try:
          results[str(sig)].append(inst)
      except NameError:
          results[str(sig)] = [inst]
      except KeyError:
          results[str(sig)] = [inst]

  # Sort instructions
  for key in results:
    results[key].sort(key=lambda inst: inst.source_lines())

  return results
 
# TODO: add API documentation 
def prettify_all_instructions(instructions):
  for sig in instructions:
    print(f"function {sig}")
    for inst in instructions[sig]:
      print(f"    {inst.source_lines()[0]}:   {inst.source_code()}")

# TODO: add API documentation 
def print_all_instructions(instructions):
  for sig in instructions:
    for inst in instructions[sig]:
      print(inst.source_code())