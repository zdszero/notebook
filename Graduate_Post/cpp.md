### 层次条件判断

```c
if (not condition1) {
  return condition1;
} else if (not condition2) {
  return condition2;
} else if (not condition3) {
  return condition3;
}
```


### 格式化输入，输出

格式化输入、输出应该使用C语言中的`scanf`, `printf`，一般的输入、输出可以采用C++中的`sstream`, `iostream`, `fstream`流的方式

#### 输入

```cpp
scanf("%d-%*d %d", num1, num2);  // %*d表示忽略第二个参数，注意最后不要加'\n'
getline(cin, s);   // 读取一行字符
```

#### 输出

`格式：%[标记][字段宽度][.精度][长度修饰符]种类`
+ 标记：默认右对齐，`-`表示左对齐
+ 字段宽度默认用空格填充

```c
printf("%-10d", number);   // 打印宽度为10，左对齐，用空格填充
printf("%04d", number);    // 打印宽度为4，默认右对齐，用0填充
printf("%*s", number, s);  // 打印宽度为number，用*作为长度的占位符
// 数字：%d %x %X %o
// 字符串：%[*]s
```

### 字符串分割

通过`getline`和`istringstream`来对字符串进行分割

```cpp
istringstream iss(s);
string tmp;
vector<string> vec;
while (getline(iss, tmp, sep)) {
  vec.push_back(tmp);
}
```

### 类型选择

给定的数据域是int对应的数据域时，如果两个数字可能相乘，应该选用`long long`类型，防止溢出

### STL

#### vector, deque, list

+ 用vector实现长度为变量的多维数组

```cpp
vector<vector<int>> vec(len1, vector<int>(len2, 0));
```

+ 使用vector的技巧

向满载的vector（size == capacity）中添加元素时，会导致编译器重新分配一块新的空间，然后复制当前vector中的所有元素，所以建议在使用vector时先用`resize`或者`reserve`申请空间，有利于提升效率。

在vector中使用`insert`和`erase`会导致大量的复制，应该尽量避免。

+ 判断键值是否存在

map: `map.count(key) == 0`或者`map.find(key) == map.end()`

vector: `find(v.begin(), v.end(), val) == v.end()`

string: `s.find(c) == string::npos`

+ 一些需要更加熟悉的函数
  + insert
    + insert(pos, elem)
    + insert(pos, n, elem)
    + insert(pos, first, last)
    + insert(pos, initlist)
  + erase
    + erase(pos)
    + eraes(begin, end)   [begin, end)

#### algorithm

注意在使用STL的函数时，尾部的迭代器应该是指向 **最后一个元素的后一个** 

+ 传入排序方式

使用函数对象

```cpp
class cmp {
public:
  bool operator() (const string &lhs, const stirng &rhs) {
    return balabala;
  }
}
```

定义一个函数传入

```cpp
[](const string &lhs, const string &rhs) {
  return balabala;
}
```

+ 一些需要熟悉的函数
  + `min_element, max_element`返回指针
  + `is_sorted`
  + `lower_bound`, `upper_bound`

+ list的特殊用法

```cpp
auto val = *(lst.begin());  // 获得第一个元素，list不能使用[] operator
lst.sort(); // 无需传入排序方式，应该在对象类中重载<
```

### 概念问答

+ CPP多态是什么？

当调用成员函数时，会根据对象的类型来执行不同的函数，可能是子类的函数，也可能是父类的函数。

+ 虚函数和纯虚函数

虚函数表示编译器将该函数设为`动态绑定`，即在调用该函数时再决定调用是父类或子类的函数，纯虚函数表示父类中不给出定义，只在子类中给出。

`virtual func() = 0; // 定义纯虚函数`

+ CPP中的接口是什么？

如果类中至少有一个函数被声明为纯虚函数，那么这个类就是抽象类。抽象类可以看作C++中的接口，抽象类不可以创造对象。
