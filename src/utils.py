# Description: extends functionality to find use cases of msg.sender

from glider import *
def query():
  instructions = Instructions().exec(10000) 
  for instruction in instructions:
    if Instruction_contains_strict_msg_sender_check(instruction):
      None
 
  return []

def process_operands(operands, embedded_expressions):
  is_embedded = False
  for op in operands:
    try:
      for ops_2 in op.get_operands():
        if ops_2.expression in embedded_expressions:
          is_embedded = True
 
        if process_operands([ops_2], embedded_expressions):
          is_embedded = True
    except:
        pass  
    
  return is_embedded

def Instruction_contains_strict_msg_sender_check(instruction):
    result = False
    if "require" in instruction.solidity_callee_names() and Instruction_calls_msg_sender(instruction):
        for ops in instruction.get_operands():
          for args in ops.get_args():
            if is_none(args):
              continue

            # TODO: we should replace try/catch with instanceOf switch statement

            # Designed for vars and mappings
            try:
              if not process_operands(args.get_operands(), msg_sender_calls()):

                # START HERE: work on this edit case and remove this false positive
                if "dx <= tokenFrom.balanceOf(msg.sender)" in instruction.source_code():
                  print(instruction)
                  print(instruction.source_code())

                result = True 
            except:
              None 

            # Designed for Calls
            try:
              uses_msg_sender = False
              for arg in args.get_args():
                if arg.expression in msg_sender_calls():
                  uses_msg_sender = True

                # Not entirely sure if this will ever be hit but I'm thinking something like require(check_msg_sender(trustor[msg.sender])) could occur
                if not process_operands(args.get_operands(), msg_sender_calls()):
                  uses_msg_sender = True 

              # TODO: we can build better recursion (including intra-function review)
            except:
              None 

    return result 

 
def is_none(obj):
  return obj == None or isinstance(obj, NoneObject)

# from glider import *

# def query():
#   instructions = Instructions().exec(100) 
#   for instruction in instructions:
#     if Instruction_calls_msg_sender(instruction):
#       print("found usage of msg.sender")

#   return []  

def Instruction_calls_msg_sender(instruction):
  result = False
 
  for vars_read in instruction.instruction_data["variables_read"]:
    if vars_read["name"] in msg_sender_calls():
      result = True 
      break
  
  return result

def msg_sender_calls():
    return [
      "msg.sender",
      "msgSender",
      "_msgSender()"
    ] 
