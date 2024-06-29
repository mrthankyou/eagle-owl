def is_none(obj):
    return obj == None or isinstance(obj, NoneObject)
 
def contains_common_element(array1, array2):
    set2 = set(array2)
    for item in array1:
        if item in set2:
            return True
    return False

# Returns the first line of a string. Works well when retrieving the contract declaration 
def get_contract_declaration(source_code):
    lines = source_code.split('\n')
    if lines:
        return lines[0]
    return ""
    