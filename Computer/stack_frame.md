### stack frame

+ C demo code

```c
int foo(int x, int y, int z) {
    int a, b ,c;
    a = 1;
    b = 2;
    c = 3;
    return a;
}
foo(10, 5, 2);
```

+ Assembly in AT&T format

```asm
# parameters
pushl 2
pushl 5
pushl 10
# function call
pushl %ebp
movl %esp, %ebp
subl $12, %esp
movl $1, -4(%ebp)
movl $2, -8(%ebp)
movl $3, -12(%ebp)
```

`push %ebp` to save the prvious stack frame base pointer, `movl %esp, %ebp` to make `%ebp`
to points to the current stack frame base.

+ stack frame

from higher address to lower address

```
:    :
| 2  | 16(%ebp)  parameter 1
| 5  | 12(%ebp)  parameter 2
| 10 | 8(%ebp)   parameter 3
| RA | 4(%ebp)   older ebp
         ebp points to here
| FP | ↙ 
| 1  | -4(%ebp)  var a
| 2  | -8(%ebp)  var b
| 3  | -12(%ebp) var c
:    : ↖ 
         esp points to here
```

+ stack in detail

after the `movl $0x11223344, (%ebp)` is executed when `%ebp = 4`

```
higher address
7 | 0x44 |
6 | 0x33 |
5 | 0x22 |   ebp points to here
4 | 0x11 | ↙ 
lower address
```

little endian is used in the previous case
