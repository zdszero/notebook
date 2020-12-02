# vim中的正则表达式

## 模式

+ `\v`: very magic, regex like perl
+ `\m`: magic, default mode, `()` and `+` are literals
+ `\M`: no magic,  `.` and `*` are literals
+ `\V`: very nomagic, other than `/` and delimeters(`^ $`)

测试文本：(... * ++ // [])  

## 字符类别

+ `\s`: space
+ `\d`: number
+ `\w`: word
+ `\a`: alphabet
+ `\h`: legal start char for variable name
+ `\l`: lowercase
+ `\u`: uppercase
+ `\t`: tab
+ `\r`: return
+ `\n`: endline
+ `\e`: \<escape\>
