# 数学运算模块：math与cmath
> python3.7
> 文档：
> https://docs.python.org/3/library/math.html
> https://docs.python.org/3/library/cmath.html

## math模块
* 其实不起眼的math里加进去了很多黑科技。

### 常规部分

#### math.ceil(x)
* 向上取整

```
>>> import math
>>> math.ceil(0.0)
0
>>> math.ceil(0.1)
1
>>> math.ceil(41.1)
42
```

#### math.copysign(x, y)
* copy符号
* 返回x的绝对值和y的符号（对不起，这是我和他的孩子）

```
>>> import math
>>> math.copysign(1, -0.0)
-1.0
>>> math.copysign(-1, 0.0)
1.0
>>> math.copysign(-1, -0.0)
-1.0
>>> math.copysign(1, 0)
1.0
```

#### math.fabs(x)
* 返回绝对值
* math.fabs()与内置函数abs()的区别：
	* fabs需要import math后才能调用，abs可以直接使用
	* abs可以用于复数而fabs不可以。

```
>>> math.fabs(-8)
8.0
>>> abs(-8)
8
>>> abs(1+1.0j)
1.4142135623730951
>>> math.fabs(1+1.0j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    math.fabs(1+1.0j)
TypeError: can't convert complex to float
```

#### math.factorial(x)
* 这个函数竟然可以返回x！
* 2乘3竟然等于3！
* （返回x的阶乘）

```
>>> math.factorial(3)
6
>>> math.factorial(10)
3628800
```

#### math.floor(x)
* 向下取整

```
>>> math.floor(0.0)
0
>>> math.floor(0.1)
0
>>> math.floor(-0.1)
-1
>>> math.floor(42.9)
42
```

#### math.fmod(x, y)
* 取模运算
* 与路人运算符号%的区别：
	* fmod默认返回浮点数
	* 对于x、y符号一致时，%与fmod结果一致
	* 但x、y符号不一致时，结果不同
	* 详见[取模运算](https://baike.baidu.com/item/%E5%8F%96%E6%A8%A1%E8%BF%90%E7%AE%97 "取模运算")

```
>>> 3%2
1
>>> 3%-2
-1
>>> -3%2
1
>>> 3.1%3
0.10000000000000009
>>> math.fmod(3, 2)
1.0
>>> math.fmod(3, -2)
1.0
>>> math.fmod(-3, 2)
-1.0
>>> math.fmod(3.1, 3)
0.10000000000000009
>>> math.fmod(-7, 4)
-3.0
>>> (-7)%4
1
>>> math.fmod(-7, -4)
-3.0
>>> (-7)%(-4)
-3
```

#### math.frexp(x)
* 将x分解为尾数与指数
`x = 尾数 * 2^指数`

```
>>> math.frexp(3)
(0.75, 2)
>>> 0.75*2**2
3.0
>>> math.frexp(32)
(0.5, 6)
>>> 0.5*2**6
32.0
>>> math.frexp(-32)
(-0.5, 6)
```

#### math.fsum(iterable)
* 功能同内置函数sum()，但精度更高

```
>>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
0.9999999999999999
>>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
1.0
```

#### math.gcd(a, b)
* 一键返回最大公约数

```
>>> math.gcd(32, 33)
1
>>> math.gcd(32, 34)
2
>>> math.gcd(32, 64)
32
```

#### math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
* “接近”判断
    abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

* 若：
	* rel_tol=x
	* abs_tol=y
* math.isclose(a, b, rel_tol=x, abs_tol=y)翻译成：
	* a与b“接近”的判定条件是：
		* a与b的差距是否小于ab较大的那个乘以x
		* 或ab差距小于y
	* 翻译v2：
		* ab，你和你女朋友
		* x你们的感情
		* y有没有房
		* “你和你女朋友会不会结婚取决于你们的感情或你们有没有房。”

```
>>> math.isclose(3,5,rel_tol=0.2, abs_tol=0.0)
False
>>> math.isclose(3,5,rel_tol=0.5, abs_tol=0.0)
True
>>> math.isclose(3,5,rel_tol=0.2, abs_tol=2.0)
True
```

#### math.isfinite(x)
* 判断x有限或者不是nan

```
>>> math.isfinite(float('nan'))
False
>>> math.isfinite(float('NaN'))
False
>>> math.isfinite(1)
True
```

#### math.isinf(x)
* 判断x是否为正负无限

#### math.isnan(x)
* 判断x是否为nan

#### math.ldexp(x, i)
* math.frexp(x)的逆运算

```
>>> math.frexp(32)
(0.5, 6)
>>> math.ldexp(0.5, 6)
32.0
```

#### math.modf(x)
* 分离x的整数和小数部分

```
>>> math.modf(3.1)
(0.10000000000000009, 3.0)
>>> math.modf(-3.3)
(-0.2999999999999998, -3.0)
```

#### math.remainder(x, y)
* 符合IEEE 754标准的求余……

```
>>> math.remainder(5, 2)
1.0
>>> math.remainder(-7, 4)
1.0
>>> math.remainder(-7, -4)
1.0
>>> math.remainder(7, 4)
-1.0
>>> math.remainder(7, -4)
-1.0
```

math.trunc(x)
* 截断x的小数部分
```
>>> math.trunc(32)
32
>>> math.trunc(32.1)
32
>>> math.trunc(32.00000000001)
32
>>> math.trunc(-233.2)
-233
```

### 指数、对数部分

#### math.exp(x)
* e为底的指数

```
>>> math.exp(0)
1.0
>>> math.exp(1)
2.718281828459045
```

#### math.expm1(x)
* math.expm1(x)=exp(x) - 1

```
>>> math.expm1(0)
0.0
>>> math.expm1(1)
1.718281828459045
```

#### math.log(x[, base])
* 对数

```
>>> math.log(math.e,math.e)
1.0
>>> math.log(1,math.e)
0.0
```

#### math.log1p(x)
* math.log1p(x)=math.log(x+1,math.e)

```
>>> math.log1p(math.e-1)
1.0
>>> math.log1p(0)
0.0
```

#### math.log2(x)
* 二为底数

```
>>> math.log2(4)
2.0
>>> math.log2(1024)
10.0
```

#### math.log10(x)
* 十为底数

```
>>> math.log10(10)
1.0
>>> math.log10(10000)
4.0
```

#### math.pow(x, y)
* 指数运算

```
>>> math.pow(2, 0)
1.0
>>> math.pow(2, 10)
1024.0
```

#### math.sqrt(x)
* 平方根运算

```
>>> math.sqrt(4)
2.0
>>> math.sqrt(16)
4.0
```

### 三角函数部分
* 运算函数皆默认以弧度值返回。

#### math.degrees(x)与math.radians(x)
* 角度与弧度的互换

#### math.acos(x)
* arc cosine

#### math.asin(x)
* arc sine

#### math.atan(x)
* arc tangent

#### math.atan2(y, x)
* 方便调节圆上计算路径的math.atan(x)

#### math.cos(x)
* cosine

#### math.sin(x)
* sine

#### math.tan(x)
* tangent

#### math.hypot(x, y)
* 勾股定理求斜边

```
>>> math.hypot(3, 4)
5.0
```

#### math.acosh(x)
* inverse hyperbolic cosine of x

#### math.asinh(x)
* inverse hyperbolic sine of x

#### math.atanh(x)
* inverse hyperbolic tangent of x

#### math.cosh(x)
* hyperbolic cosine of x

#### math.sinh(x)
* hyperbolic sine of x

#### math.tanh(x)
* hyperbolic tangent of x

### 特殊函数部分

#### math.erf(x)
* 返回x处的误差函数

#### math.erfc(x)
* 返回x处的互补误差函数
* math.erfc(x)= 1.0-math.erf(x)

#### math.gamma(x)
* 返回x处的gamma函数

#### math.lgamma(x)
* 返回x处的自然对数gamma函数

```
>>> math.log(math.gamma(3))
0.6931471805599453
>>> math.lgamma(3)
0.693147180559945
```

### 常数部分

#### math.pi
* 宇宙真理1

#### math.e
* 宇宙真理2

#### math.tau
* 两倍的宇宙真理1
* math.tau=math.pi*2

#### math.inf
* 正无穷，加个负号变负无穷
* 可以直接用float('inf')表达

```
>>> math.isinf(float('inf'))
True
>>> math.isinf(math.inf)
True
```

#### math.nan
* not a number
* 一般见于上限爆了等神秘操作
* 可直接用float('nan')表达


## cmath模块

* cmath模块旨在进行复数运算。

### 坐标转换

#### cmath.phase(x)
* 复数的角度
```
>>> phase(complex(-1.0, 0.0))
3.141592653589793
>>> phase(complex(-1.0, -0.0))
-3.141592653589793
```

#### cmath.polar(x)
* 复数转为极坐标
* polar(x)=(abs(x), phase(x))

#### cmath.rect(r, phi)
* 极坐标转换成普通复数形式
    r * (math.cos(phi) + math.sin(phi)*1j)

### 指数对数部分

#### cmath.exp(x)
* 复数版本

#### cmath.log(x[, base])
* 复数版本

#### cmath.log10(x)
* 复数版本

#### cmath.sqrt(x)
* 复数版本

### 三角函数部分

#### cmath.acos(x)
* 复数版本

#### cmath.asin(x)
* 复数版本

#### cmath.atan(x)
* 复数版本

#### cmath.cos(x)
* 复数版本

#### cmath.sin(x)
* 复数版本

#### cmath.tan(x)
* 复数版本

#### cmath.acosh(x)
* 复数版本

#### cmath.asinh(x)
* 复数版本

#### cmath.atanh(x)
* 复数版本

#### cmath.cosh(x)
* 复数版本

#### cmath.sinh(x)
* 复数版本

#### cmath.tanh(x)
* 复数版本


### 判断部分
#### cmath.isfinite(x)
* 实虚全有限才为True

#### cmath.isinf(x)
* 实虚任意一个为infinity即为True

#### cmath.isnan(x)
* 实虚任意一个为nan即为True

#### cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
* 同math版本，用abs比较故不受影响

### 常数部分

#### cmath.pi
* 同math版本

#### cmath.e
* 同math版本

#### cmath.tau
* 同math版本

#### cmath.inf
* 同math版本

#### cmath.infj
* inf的虚部版本
    complex(0.0, float('inf'))

#### cmath.nan
* 同math版本

#### cmath.nanj
* nan虚部版本
    complex(0.0, float('nan'))