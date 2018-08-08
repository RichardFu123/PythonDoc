# 操作函数模块operator
> python3.7
> 文档：
> https://docs.python.org/3/library/operator.html

* 这个模块为常规的python运算操作符提供了对应的函数。
* 各函数本身功能与运算符一致，但在一些特殊情况下依然需要调用这个模块。
* 调用情况常见于使用某些迭代器中。


## 常用对照速查表

|实际操作|运算符|对应函数|
|:--:|:--:|:--:|
|加|a + b|add(a, b)|
|串联列表|seq1 + seq2|concat(seq1, seq2)|
|查询包含|obj in seq|contains(seq, obj)|
|除|a / b|truediv(a, b)|
|除|a // b|floordiv(a, b)|
|位与|a & b|and_(a, b)|
|位异或|a ^ b|xor(a, b)|
|位反|~ a|invert(a)|
|位或|a &#124; b|or_(a, b)|
|指数|a ** b|pow(a, b)|
|判断|a is b|is_(a, b)|
|判断|a is not b|is_not(a, b)|
|索引赋值|obj[k] = v|setitem(obj, k, v)|
|索引删除|del obj[k]|delitem(obj, k)|
|索引查询|obj[k]|getitem(obj, k)|
|位左移|a << b|lshift(a, b)|
|模|a % b|mod(a, b)|
|乘|a * b|mul(a, b)|
|矩阵乘（存在bug）|a @ b|matmul(a, b)|
|算数取反|- a|neg(a)|
|逻辑取反|not a|not_(a)|
|取正|+ a|pos(a)|
|位右移|a >> b|rshift(a, b)|
|切片赋值|seq[i:j] = values|setitem(seq, slice(i, j), values)|
|切片删除|del seq[i:j]|delitem(seq, slice(i, j))|
|切片|seq[i:j]|getitem(seq, slice(i, j))|
|格式化字符串|s % obj|mod(s, obj)|
|减|a - b|sub(a, b)|
|为真检验|obj|truth(obj)|
|大小判断|a < b|lt(a, b)|
|大小判断|a <= b|le(a, b)|
|相等判断|a == b|eq(a, b)|
|不等判断|a != b|ne(a, b)|
|大小判断|a >= b|ge(a, b)|
|大小判断|a > b|gt(a, b)|

## 成员介绍

* 由于全部概念与运算符没有偏差，所以从简。

### 特殊操作

**operator.attrgetter(attr)
operator.attrgetter(*attrs)**
* 调用操作（.）
```
>>> from operator import *
>>> import math
>>> a=attrgetter('pi')
>>> a(math)
3.141592653589793
>>> b=attrgetter('pi','e')
>>> b(math)
(3.141592653589793, 2.718281828459045)
```

**operator.itemgetter(item)
operator.itemgetter(*items)**
* 索引查询（[item]）
```
>>> data=[1,69,76,42,777,233]
>>> c=itemgetter(4)
>>> c(data)
777
>>> d(data)
>>> d=itemgetter(0,1,1,2)
(1, 69, 69, 76)
```

**operator.methodcaller(name[, args...])**
* 可带参数的attrgetter
>After **f = methodcaller('name')**, the call **f(b)** returns **b.name()**.
>After **f = methodcaller('name', 'foo', bar=1)**, the call **f(b)** returns **b.name('foo', bar=1)**.

**operator.index(a)**
* 返回整数a

**operator.concat(a, b)**
* 串联列表

**operator.delitem(a, b)**
* 列表删除元素

**operator.getitem(a, b)**
* 索引查询

**operator.indexOf(a, b)**
* 查询索引

**operator.setitem(a, b, c)**
* 索引赋值

**operator.length_hint(obj, default=0)**
* 长度查询


### 数值运算

**operator.abs(obj)**
* 取绝对值

**operator.add(a, b)**
* a + b

**operator.and_(a, b)**
* 按位与

**operator.floordiv(a, b)**
* a // b

**operator.inv(obj)
operator.invert(obj)**
* 按位取反

**operator.lshift(a, b)**
* 位左移

**operator.mod(a, b)**
* a % b

**operator.mul(a, b)**
* a * b

**operator.matmul(a, b)**
* a @ b

**operator.neg(obj)**
* 取负

**operator.or_(a, b)**
* 按位或

**operator.pos(obj)**
* 取正

**operator.pow(a, b)**
* a ** b

**operator.rshift(a, b)**
* 位右移

**operator.sub(a, b)**
* a - b

**operator.truediv(a, b)**
* 浮点除

**operator.xor(a, b)**
* 按位异或


### 赋值运算

**operator.iadd(a, b)**
* a = iadd(a, b) 等于 a += b.

**operator.iand(a, b)**
* a = iand(a, b) 等于 a &= b.

**operator.iconcat(a, b)**
* a = iconcat(a, b) 等于 a += b for a and b sequences.

**operator.ifloordiv(a, b)**
* a = ifloordiv(a, b) 等于 a //= b.

**operator.ilshift(a, b)**
* a = ilshift(a, b) 等于 a <<= b.

**operator.imod(a, b)**
* a = imod(a, b) 等于 a %= b.

**operator.imul(a, b)**
* a = imul(a, b) 等于 a *= b.

**operator.imatmul(a, b)**
* a = imatmul(a, b) 等于 a @= b.

**operator.ior(a, b)**
* a = ior(a, b) 等于 a |= b.

**operator.ipow(a, b)**
* a = ipow(a, b) 等于 a **= b.

**operator.irshift(a, b)**
* a = irshift(a, b) 等于 a >>= b.

**operator.isub(a, b)**
* a = isub(a, b) 等于 a -= b.

**operator.itruediv(a, b)**
* a = itruediv(a, b) 等于 a /= b.

**operator.ixor(a, b)**
* a = ixor(a, b) 等于 a ^= b.


### 比较运算

**operator.lt(a, b)**
* 等于 a < b

**operator.le(a, b)**
* 等于 a <= b

**operator.eq(a, b)**
* 等于 a == b

**operator.ne(a, b)**
* 等于 a != b

**operator.ge(a, b)**
* 等于 a >= b

**operator.gt(a, b)**
* 等于 a > b

### 逻辑运算

**operator.not_(obj)**
* 逻辑取反

**operator.truth(obj)**
* 真伪判断

**operator.is_(a, b)**
* 等同判断

**operator.is_not(a, b)**
* 不等判断

**operator.contains(a, b)**
* 包含判断

**operator.countOf(a, b)**
* 包含计数

