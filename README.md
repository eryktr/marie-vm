# marie-vm

## Introduction
This project hosts a virtual machine that implements the MARIE (Machine Architecture that is Really Intuitive and Easy)
architecture. It allows you to:

1. Execute any file written directly in `MARIE` assembly
2. Run any such file in `debug mode` (You can get information about the content of memory, registers, etc.)
3. Find out the overall cost of your program (There are faster and slower instructions. 
For example, reading from memory takes ages compared to reading from registers.)

## MARIE Specification

1. It only supports **integers**, represented using the **Two's complement** format
(both positive and negative numbers are supported)
2. Each word is **2 bytes** long
3. It has the following registers:

    | Mnemonic | Name         | Size (bit) |
    | ---      | ----         | ----       |
    |  AC      | Accumulator  | 16         |
    |  IR      | Instruction Register | 16 |
    | MBR      | Memory Buffer Register | 16 |
    | PC       | Program Counter | 12 |
    | MAR      | Memory Address Register | 12 |
    |          | Output Register        | 8 |
    |          | Input Register         | 8 |

### Instructions

|Instruction | Description | Action|
|   ---       | ---         | ---- |
|    JnS X       | Store the PC ad address X. |  `PC <- PC + 1`     |
|     Load X       | Load value at address X into **AC** |      `AC <- X ` |       |
| Store X       | Store the value at address X into **AC** | `X <- AC` |
| Add X     | Increase the value at **AC** by the value **at address X** (Notice that the value is not increased by X!) | `AC <- AC + X` |
| Subt X    | Similar as above - the value at **AC** is decreased.  | `AC <- AC - X` |
| Input     | Read a value from the input. Store it into **AC** | `AC <- stdin` |
| Output    | Output the value in AC to the display     | `stdout <- AC` |
| Halt      | Terminate the program. No further instructions will be executed. | `PC <- $` |
| Skipcond 000 | Skip the next instruction if AC < 0 |  `PC <- PC + 1 if AC < 0` |
| Skipcond 400 | Skip the next instruction if AC = 0 | `PC <- PC + 1 if AC == 0` |
| Skipcond 800 | Skip the next instruction if AC > 0 | `PC <- PC + 1 if AC > 0` |
| Jump X       | Move directly into instruction number X | `PC <- X` |
| Clear        | Reset **AC** by setting it to zero.     | `AC <- 0` |
| AddI X    | Use value of X as address of operand to add to `AC` | `AC <- [x]` |
| StoreI X  | Use value of X as address of address (... example in later section) to store `AC` | `[X] <- AC` |
| LoadI X   | Use value of X as address of address to load into `AC` | `AC <- [X]` |
| JumpI X   | Use value of X as address of address to jump to |      `PC <- [X]` |

### Labels
Normally, the instruction number refers to the address in memory where the content of the instruction is stored. 
Counting starts from `0`. For example, in the below program, the line `Dec 1` will be assigned address `4`, line `Dec 2`
address `5`.

If we were to write these addresses manually every time we write a program, it would become tedious in no time.
Every change (such as adding a piece of code in-between) would result in a need to rewrite addressing.
What if we had a few dozen variables?
```
Load X
Add Y
Store Z
Halt

X, Dec 1
Y, Dec 2
Z, Dec 0
```
To solve this problem, we can use **labels**. The syntax is as follows:

```
label_name, instruction
```
Notice the comma - it is a must.

```
AnswerToEverything, Dec 42
```

### Compilation and interpreter
Both, compilation and interpretation steps are used within the life cycle of MARIE code. The first phase of code is the
compilation. The main purpose of the compilation is to dispose of labels and replace them with hard-coded values.
For example, the above program, after compilation, would look like this:

```
000     Load 004
001     Add 005
002     Store 006
003     Halt

004     Dec 1
005     Dec 2
006     Dec 0
```

Now, the label-free code can be executed on the virtual machine.