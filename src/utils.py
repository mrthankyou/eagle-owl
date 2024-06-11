from glider import *

def is_none(obj):
    return obj == None or isinstance(obj, NoneObject)
 
def contains_common_element(array1, array2):
    set2 = set(array2)
    for item in array1:
        if item in set2:
            return True
    return False
