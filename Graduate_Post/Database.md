### 什么是数据库

### 数据库模型（两类数据模型）

+ 概念模型，按照用户的观点对数据和信息建模，比如`E-R图`
+ 逻辑模型，物理模型
  + 逻辑模型按照计算机系统的观点对数据建模，展现了数据之间的逻辑关系。包含层次模型、网状模型、关系模型、对象关系数据模型。
  + 物理模型是对数据底层的抽象，描述数据在数据库系统内部的表达方式和存取方法。

### 关系

#### 什么是关系模型

用关系来表示数据结构的模型，关系在用户看来，就是一张二维表。

#### 基本的关系操作

query, insert, update, delete

#### 查询的基本操作

+ 选择（select）
+ 投影（project）
+ 连接（join）
+ 除（divide）
+ 并（union）
+ 差（except）
+ 交（intersection）
+ 笛卡尔积

#### 主键和外键

数据库中的表通过键将彼此之间联系起来。主键是关系表中的一个列，在这个列中每一行的值都是唯一的。只有这样，才能保证在不重复的情况下，将表间的数据交叉捆绑在一起。

#### 实例

```sql
-- like
select * from Persons where City is like 'N%'
select * from Persons where City is like '%lon%'
-- in
select * from Persons where Lastname in ('Adams', 'Carter')
-- between
select * from Persons where Grade between 80 and 90
-- join
select Person.Lastname,Person.Firstname,Orders.Orderno from Persons, Orders where Persons.Id_P = Orders.Id_P

```

### 事务

#### 特性

+ 原子性：事务要不全做，要不全不做。
+ 一致性：比如转账和入账要同时进行，要么全做，要么全不做。与原子性密切相关。
+ 隔离性：一个事务的内部操作及使用的数据对其他事务是隔离的，并发执行的各个事务不能互相干扰。
+ 持续性：一个事务一旦提交，它对数据库中数据的改变是永久性的。
