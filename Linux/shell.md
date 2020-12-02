# variable

+ 全局变量：default
+ 局部变量：local，函数内部
+ 环境变量：export，子进程中也有效

# condition test

## && || & ;

```sh
[ -z $EDITOR ] && echo $EDITOR
echo 'hello'; echo 'world'
```

## [] test

+ 文件

1. 类型

```
-f file
-d directory
-b block file
-c character file
-p pipe file
-L symbolic link
-S socket file
```

2. 权限

```
-r readable?
-w writable?
-x executable?
```

3. 比较

```
-ot older than
-nt newer than
-ef same inode?
```

+ 数值比较

```
-eq -ne -ge -gt -le -lt
```

+ 字符串

```
-z  string == '' ?
-n  string != '' ?
= 或者 ==  判断字符串是否相等
```

+ 逻辑运算

```
-a and
-o or
! not
```

## [[]]

在使用test或[]是，需要对变量引用加上双引号`"$val"`，走则会出现很多奇怪的问题。

[[]]是shell内的关键字，与[]不同，在使用时没有向函数传递参数的过程，主要有以下特点：
+ 不需要对变量加上双引号
+ 支持逻辑运算符和正则表达式
+ 对数字处理不友好

+ 逻辑运算符

```sh
if [[ -z $str1 ]] || [[ -z $str2 ]]
if [[ -z $str1 || -z $str2 ]]
if [ -z "$str1" -o -z "$str2" ]
```

# array

+ create

```sh
files=(ls)
nums=(1 2 3 4)
```

+ element

```sh
${arr[3]}  $arr[3]
```

+ length

```sh
${#arr[@]}
${#arr[*]}
```

# function

+ create

```sh
function fn {}
function fn() {}
fn() {}
```

+ special variables

```
$0 filename
$n the nth parameter
$# parameter count
$@ all parameters：数据和数据之间独立
$* all parameters：整体看成一份数据
$? the last command exit status
```
