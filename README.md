
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
    - [get\_all\_instructions(Function) -\> \[String\]\[\]Instruction](#get_all_instructionsfunction---stringinstruction)
  - [Message Sender instructions](#message-sender-instructions)
    - [WIP - instruction\_calls\_msg\_sender(Instruction) -\> Bool](#wip---instruction_calls_msg_senderinstruction---bool)
    - [WIP - instruction\_contains\_direct\_msg\_sender\_check(Instruction) -\> Bool](#wip---instruction_contains_direct_msg_sender_checkinstruction---bool)


# API Documentation

> Note: This documentation and code is a WIP.

## Utilities

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

### get_all_instructions(Function) -> [String][]Instruction

This function returns all instructions within a Function. This includes all intra-instructions. For example, if you pass in the Function:

```solidity
function transferFrom(
    address sender,address recipient,uint256 amount
) public virtual override returns (bool) {
    _transfer(sender,recipient,amount);

    uint256 currentAllowance = _allowances[sender][_msgSender()];
    require(currentAllowance >= amount,"ERC20: transfer amount exceeds allowance");
    unchecked {
        _approve(sender,_msgSender(),currentAllowance - amount);
    }

    return true;
}
```

The instructions returned will include everything in `transferFrom` as well as `_transfer()` and `_approve()`.

The return value is a dictionary where the key represents the function signature and each value is an array of Instructions. For example:

```python
{
  'onERC721Received(address,address,uint256,bytes)': [
    <api.instructions.ExpressionInstruction object at 0x7f75eb95c250>, 
    <api.instructions.NewVariableInstruction object at 0x7f75eb95cb50>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb95cd90>, 
    <api.instructions.NewVariableInstruction object at 0x7f75eb95ccd0>, 
    <api.instructions.NewVariableInstruction object at 0x7f75eb95cd30>, 
    <api.instructions.NewVariableInstruction object at 0x7f75eb95cb20>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb95cc10>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb95cca0>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb95ce50>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb95cee0>, 
    <api.instructions.ReturnInstruction object at 0x7f75eb95cf70>
  ], 
  'checkMatchingAttributes(string,uint16)': [
    <api.instructions.NewVariableInstruction object at 0x7f75eb9e4550>, 
    <api.instructions.NewVariableInstruction object at 0x7f75eb9e43d0>, 
    <api.instructions.IfInstruction object at 0x7f75eb9e4850>, 
    <api.instructions.ReturnInstruction object at 0x7f75eb9e4a30>, 
    <api.instructions.ReturnInstruction object at 0x7f75eb9e44f0>
  ],
  '_mint(address,uint256)': [
    <api.instructions.ExpressionInstruction object at 0x7f75eb99b2e0>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb99b010>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb99b520>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb99b700>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb99b1c0>, 
    <api.instructions.ExpressionInstruction object at 0x7f75eb99b6a0>
  ]
}
```

> Note: This function does sort Instructions within each Function but does not sort each Function based on when it's called. This will be fixed at a later time.




## Message Sender instructions

### WIP - instruction_calls_msg_sender(Instruction) -> Bool

This function is used to determine whether `msg.sender` or any variation of it is called in an instruction. For example, the following instructions will return true:

```solidity
require(msg.sender != address(0), "No empty accounts allowed"); // returns true

owner = msgSender; // returns true

approvedAccounts[_msgSender()] = true; // returns true

```

This function accepts an instruction object.


### WIP - instruction_contains_direct_msg_sender_check(Instruction) -> Bool

This function is used to determine whether msg.sender is strictly used in a require statement. For example, the following instruction passed into this function will return true:

```solidity
require(msg.sender == owner);
```

This function accepts an instruction object.

