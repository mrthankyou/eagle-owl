# API

> Note: This documentation and code is a WIP.

- [API](#api)
  - [Message Sender instructions](#message-sender-instructions)
    - [instruction\_calls\_msg\_sender(Instruction) -\> Bool](#instruction_calls_msg_senderinstruction---bool)
    - [instruction\_contains\_direct\_msg\_sender\_check(Instruction) -\> Bool](#instruction_contains_direct_msg_sender_checkinstruction---bool)
  - [Utils](#utils)
    - [is\_none(Any) -\> Bool](#is_noneany---bool)
    - [find\_reverts(\[\]Instruction) -\> \[\]Instruction](#find_revertsinstruction---instruction)
    - [has\_reverts(\[\]Instruction) -\> Bool](#has_revertsinstruction---bool)
    - [find\_requires(\[\]Instruction) -\> \[\]Instruction](#find_requiresinstruction---instruction)
    - [has\_requires(\[\]Instruction) -\> Bool](#has_requiresinstruction---bool)
    - [intra\_instructions(Function) -\> \[\]Instruction](#intra_instructionsfunction---instruction)

## Message Sender instructions

### instruction_calls_msg_sender(Instruction) -> Bool

This function is used to determine whether `msg.sender` or any variation of it is called in an instruction. For example, the following instructions will return true:

```solidity
require(msg.sender != address(0), "No empty accounts allowed"); // returns true

owner = msgSender; // returns true

approvedAccounts[_msgSender()] = true; // returns true

```

This function accepts an instruction object.


### instruction_contains_direct_msg_sender_check(Instruction) -> Bool

This function is used to determine whether msg.sender is strictly used in a require statement. For example, the following instruction passed into this function will return true:

```solidity
require(msg.sender == owner);
```

This function accepts an instruction object.


## Utils

### is_none(Any) -> Bool

This function is used to determine if an object is None or NoneType. If it is, it returns true, otherwise it returns false.

This function accepts any argument.

### find_reverts([]Instruction) -> []Instruction

This function is used to filter all instructions that contain reverts.


### has_reverts([]Instruction) -> Bool

This function returns a boolean if an array of instructions contain any reverts.


### find_requires([]Instruction) -> []Instruction

This function is used to filter all instructions that contain requires.


### has_requires([]Instruction) -> Bool

This function returns a boolean if an array of instructions contain any requires.

### intra_instructions(Function) -> []Instruction

WIP

This function returns all instructions (including intra-instructions) for a given function. 

