# Description: extends functionality to find use cases of msg.sender

# from glider import *
# def query():
#   instructions = Instructions().exec(100) 
#   for instruction in instructions:
#     if Instruction_calls_msg_sender(instruction):
#       print("found usage of msg.sender")
#   return []


def Instruction_calls_msg_sender(instruction):
  msg_sender_types = [
    "msg.sender",
    "msgSender",
    "_msgSender()"
  ]

  result = False

  for op in instruction.get_operands():
    if op.expression in msg_sender_types:
      result = True
      break
  
  return result
