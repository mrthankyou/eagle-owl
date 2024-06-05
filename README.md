
# Eagle Owl - A helper library for writing Glides

Eagle Owl is designed to aid Gliders writing glides on Remedy's Glider platform.

> Note: This is a WIP. All code is temporary. Suggestions and feedback is welcome through Github issues.

## How To Use 

It is currently recommended if you want to use any of the functions to copy and paste the entire python file that contains the function into your query. Once more work is done on this project there will be a better solution provided. Apologizes in advance.

## Contact

Any feature/bug requests can be made through Github issues. I will do my best to be as responsive as I can. Thanks!

## Table of Contents

- [Eagle Owl - A helper library for writing Glides](#eagle-owl---a-helper-library-for-writing-glides)
  - [How To Use](#how-to-use)
  - [Contact](#contact)
  - [Table of Contents](#table-of-contents)
- [API Documentation](#api-documentation)
  - [Utilities](#utilities)
    - [is\_none(Any) -\> Bool](#is_noneany---bool)
    - [find\_reverts(\[\]Instruction) -\> \[\]Instruction](#find_revertsinstruction---instruction)
    - [has\_reverts(\[\]Instruction) -\> Bool](#has_revertsinstruction---bool)
    - [find\_requires(\[\]Instruction) -\> \[\]Instruction](#find_requiresinstruction---instruction)
    - [has\_requires(\[\]Instruction) -\> Bool](#has_requiresinstruction---bool)
  - [Instructions](#instructions)
    - [find\_root\_variable(Instruction) -\> Value | None](#find_root_variableinstruction---value--none)
    - [find\_root\_call(Instruction) -\> Value | None](#find_root_callinstruction---value--none)
    - [get\_if\_else\_instructions(Instruction) -\> \[\]Instruction](#get_if_else_instructionsinstruction---instruction)
  - [State Variables](#state-variables)
    - [get\_state\_variable\_write\_instructions(StateVariable) -\> \[\]Instruction](#get_state_variable_write_instructionsstatevariable---instruction)
  - [Context Library](#context-library)
    - [msg\_sender\_calls() -\> \[\]String](#msg_sender_calls---string)


# API Documentation

> Note: This documentation and code is a WIP.

## Utilities

### is_none(Any) -> Bool

Returns a boolean if an object is None or NoneType. If it is None, the function returns true.Otherwise it returns false.

This function accepts any argument.

### find_reverts([]Instruction) -> []Instruction

Filter all Instructions that contain reverts.

### has_reverts([]Instruction) -> Bool

Returns a boolean if an array of Instructions contain any reverts.


### find_requires([]Instruction) -> []Instruction

Filters all Instructions that contain requires.


### has_requires([]Instruction) -> Bool

Returns a boolean if an array of Instructions contain any requires.

## Instructions

### find_root_variable(Instruction) -> Value | None

Returns the root variable (aka Value) from the instruction.

For example, the following instruction passed into the function will return `token`.:

```solidity
token.safeTransfer(msg.sender, 100)
```

### find_root_call(Instruction) -> Value | None

Returns the root call from the instruction.

For example, the following instruction passed into the function will return `token.balanceOf(msg.sender)`.:

```solidity
token.balanceOf(msg.sender).add(100)
```

### get_if_else_instructions(Instruction) -> []Instruction

Returns the instructions within an if/else statement. If the Instruction argument is not an if instruction, the if instrution is returned.

## State Variables

### get_state_variable_write_instructions(StateVariable) -> []Instruction

This function is used to retrieve all Storage Write Instructions that write to a State Variable. 

This function accepts a State Variable as the single argument



## Context Library

Adds utility functions for working with libraries

### msg_sender_calls() -> []String

Returns a list of common functions and variables that represent msg.sender.

