# API

> Note: This documentation and code is a WIP.

## Instruction checks

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

The `is_none` function is used to determine if an object is None or NoneType. If it is, it returns true, otherwise it returns false.

This function accepts any argument.

