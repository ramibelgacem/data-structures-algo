# String operations

This algorithm performs operations on a stack. A string of numbers and operators as in input.

## Operations

- `[0..2^10]`: push the number onto the stack
- `+`: pop the two topmost values from the stack, add them and push the result back onto the stack
- `-`: pop the two topmost values from the stack, substruct them and push the result back onto the stack
- `DUP`: duplicate the last element of the stack
- `POP`: delete the last element of the stack

We can not apply operations on an empty stack.

We can not apply addition and sbstruction operations on a stack with one element.

Report an error if any operation (addition or multiplication) results an overflow.

**Result**:

- Return the topmost value of the stack.
- Return -1 if the system report an error.
- Return -1 if we get an empty stack at the end.

**Example**:

Input: "5 6 DUP POP 1 + 8 -"

| character |         comment          | stack |
|-----------|--------------------------|-------|
| 5         | push 5 onto the stack    | 5     |
| 6         | push 6 onto the stack    | 5 6   |
| DUP       | apply duplication        | 5 6 6 |
| POP       | pop the topmost element  | 5 6   |
| 1         | push 1 onto the stack    | 5 6 1 |
| +         | apply addition           | 5 7   |
| 8         | push 1 onto the stack    | 5 7 8 |
| -         | apply substruction       | 5 1   |

The system returns 1 as a result
