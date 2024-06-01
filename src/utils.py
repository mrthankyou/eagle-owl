from glider import *

def get_func_instructions(func):
    return func.instructions().exec()

def get_funcs_from_instructions(insts):
    results = []
    for inst in insts:
        if is_none(inst):
            continue
        for callee in inst.get_callee_values():
            if is_none(callee):
                continue
            results.append(callee.get_function())
    return results

def recursive_call(func):
    insts = get_func_instructions(func)
    result = []
    for inst in insts:
        funcs = get_funcs_from_instructions([inst])
        nested_funcs = []
        for nested_func in funcs:
            if is_none(nested_func):
                continue
            nested_funcs.append(recursive_call(nested_func))
        result.append({
            'instruction': inst,
            'funcs': nested_funcs
        })
    return result

def master_call(func):
    return {str(func.name): recursive_call(func)}

def query():
    funcs = Functions().with_name("purchase").exec(1)
    func = funcs[0]
    result = master_call(func)

    print_instructions_with_source_code(result)

    return []

def is_none(obj):
    return obj == None or isinstance(obj, NoneObject)
 

def print_instructions_with_source_code(result, indent=0):
    def print_nested_instructions(instructions, indent):
        indent_str = '  ' * indent
        for instruction_dict in instructions:
            instruction = instruction_dict['instruction']
            source_code = instruction.source_code()
            print(f"{indent_str}Instruction: {source_code}")
            nested_funcs = instruction_dict['funcs']
            if nested_funcs:
                print_nested_instructions(nested_funcs, indent + 1)

    indent_str = '  ' * indent
    for func_name, instructions in result.items():
        print(f"{indent_str}Function: {func_name}")
        print_nested_instructions(instructions, indent + 1)
 