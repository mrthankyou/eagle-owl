
# Eagle Owl - A helper library for writing Glides

Eagle Owl is designed to aid Gliders writing glides on Remedy's Glider platform.

> Note: This is a WIP. All code is temporary. Suggestions and feedback are welcome through Github issues.

## How To Use 

If you want to use any of the functions, please copy and paste the entire python file that contains the function into your query. Once more work is done on this project there will be a better solution provided. Apologizes in advance.

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
    - [contains\_common\_element(Any\[\], Any\[\]) -\> Bool](#contains_common_elementany-any---bool)
  - [Instructions](#instructions)
    - [find\_reverts(\[\]Instruction) -\> \[\]Instruction](#find_revertsinstruction---instruction)
    - [has\_reverts(\[\]Instruction) -\> Bool](#has_revertsinstruction---bool)
    - [find\_requires(\[\]Instruction) -\> \[\]Instruction](#find_requiresinstruction---instruction)
    - [has\_requires(\[\]Instruction) -\> Bool](#has_requiresinstruction---bool)
    - [find\_asserts(\[\]Instruction) -\> \[\]Instruction](#find_assertsinstruction---instruction)
    - [has\_asserts(\[\]Instruction) -\> Bool](#has_assertsinstruction---bool)
    - [sort\_instructions\_by\_source\_line(\[\]Instruction) -\> \[\]Instruction](#sort_instructions_by_source_lineinstruction---instruction)
  - [Instruction](#instruction)
    - [find\_root\_variable(Instruction) -\> Value | None](#find_root_variableinstruction---value--none)
    - [find\_root\_call(Instruction) -\> Value | None](#find_root_callinstruction---value--none)
    - [find\_call\_in\_instruction(Instruction, str) -\> Call | None](#find_call_in_instructioninstruction-str---call--none)
    - [is\_new\_var\_instruction(Instruction) -\> Bool](#is_new_var_instructioninstruction---bool)
    - [is\_require\_statement(Instruction) -\> Bool](#is_require_statementinstruction---bool)
  - [Functions](#functions)
    - [is\_interface\_function(Function) -\> Bool](#is_interface_functionfunction---bool)
  - [Condition](#condition)
    - [get\_conditional\_statements(\[\]Operands, String, String, String) -\> \[\]\[\]Op](#get_conditional_statementsoperands-string-string-string---op)
  - [State Variables](#state-variables)
    - [get\_state\_variable\_write\_instructions(StateVariable) -\> \[\]Instruction](#get_state_variable_write_instructionsstatevariable---instruction)
  - [Values](#values)
    - [get\_value\_type(Value) -\> String | None](#get_value_typevalue---string--none)
  - [Context Library](#context-library)
    - [msg\_sender\_calls() -\> \[\]String](#msg_sender_calls---string)
  - [Math library](#math-library)
    - [math\_subtraction\_function\_names() -\> \[\]String](#math_subtraction_function_names---string)


# API Documentation

> Note: This documentation and code is a WIP.

## Utilities

### is_none(Any) -> Bool

Returns a boolean if an object is None or NoneType. If it is None, the function returns true.Otherwise it returns false.

This function accepts any argument.

### contains_common_element(Any[], Any[]) -> Bool

Returns true if any item from Array A exists in Array B. 

The first argument is represented as Array A and the second argument is Array B.


## Instructions

### find_reverts([]Instruction) -> []Instruction

Filter all Instructions that contain reverts.

### has_reverts([]Instruction) -> Bool

Returns a boolean if an array of Instructions contain any reverts.

### find_requires([]Instruction) -> []Instruction

Filters all Instructions that contain requires.

### has_requires([]Instruction) -> Bool

Returns a boolean if an array of Instructions contain any requires.

### find_asserts([]Instruction) -> []Instruction

Filters all Instructions that contain asserts.

### has_asserts([]Instruction) -> Bool

Returns a boolean if an array of Instructions contain any asserts.

### sort_instructions_by_source_line([]Instruction) -> []Instruction 

Returns a list of instructions sorted by the starting source lines.

Note: EntryPointInstructions may not be guaranteed to be the first item. You may consider filtering out EntryPointInstructions if you desire. 

## Instruction

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

### find_call_in_instruction(Instruction, str) -> Call | None

Given the name of a call, find the Call in a given Instruction. If no calls are found, None is returned.

The first argument represents the instruction to search in. The second argument represents the call name.

### is_new_var_instruction(Instruction) -> Bool

Returns true or false if the Instruction is a new var. 

### is_require_statement(Instruction) -> Bool

Returns true or false if the Instruction contains a require statement.

## Functions

### is_interface_function(Function) -> Bool

Returns true or false if the Function is an interface function.

The Function passed into this function is considered an interface function if the function contains no instructions. There is a possibility that a function defined in a contract may return true here. That said, from a querier's perspective, I believe that there is no difference between an interface function and a contract function with no body.

## Condition

### get_conditional_statements([]Operands, String, String, String) -> [][]Op

Returns an array of conditions given a set of search criteria. 

A description of arguments is below:

- The first argument is an array of Operands which consists of all the Operands you want to look at. You can get the array of Operands via calling Instruction_Instance.get_operands().
- The second argument represents the expression value of `a`. Consider the following example: `a < b`. If you want to find this condition, set the second argument to `a`.
- The third argument represents the operand of the condition. For example, `>`, `>=`, '<', etc.
- The fourth argument represents the expression value of `b`. Consider the following example: `a < b`. If you want to find this condition, set the second argument to `b`.

The return value will equal an array where each array item represents the condition found. 

To provide a more high-level example, considering the following Instruction:

```solidity
require(balance < 1e18, "low balance")
```

By running `get_conditional_statements(instruction.get_operands(), 'balance', <, '1e18')`, you will receive an array with a single item. Within that item is an array of Operands which represent `balance`, `<`, and `1e18`.

## State Variables

### get_state_variable_write_instructions(StateVariable) -> []Instruction

This function is used to retrieve all Storage Write Instructions that write to a State Variable. 

This function accepts a State Variable as the single argument



## Values

### get_value_type(Value) -> String | None 

This function returns the type for a given Value, rather the Value is a Var, Literal, or ValueExpression. If the function is unable to determine the type, None is returned.

Please note that due to the complexity and varieties of a ValueExpression, this function is limited to returning ValueExpressions for struct attributes and arrays.


## Context Library

Adds utility functions for working with libraries

### msg_sender_calls() -> []String

Returns a list of common functions and variables that represent msg.sender.

## Math library

### math_subtraction_function_names() -> []String

Returns an array of common subtraction function names in various popular Math libraries.
