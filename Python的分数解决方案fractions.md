# 分数模块fractions
> python3.7
> 手册：
> https://docs.python.org/3/library/fractions.html

### 介绍
* fractions模块专门为计算分数而设计。
* 可以方便地由其他模式直接转换。

```
>>> from fractions import Fraction
>>> Fraction(16, -10)
Fraction(-8, 5)
>>> Fraction(123)
Fraction(123, 1)
>>> Fraction()
Fraction(0, 1)
>>> Fraction('3/7')
Fraction(3, 7)
>>> Fraction(' -3/7 ')
Fraction(-3, 7)
>>> Fraction('1.414213 \t\n')
Fraction(1414213, 1000000)
>>> Fraction('-.125')
Fraction(-1, 8)
>>> Fraction('7e-6')
Fraction(7, 1000000)
>>> Fraction(2.25)
Fraction(9, 4)
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> from decimal import Decimal
>>> Fraction(Decimal('1.1'))
Fraction(11, 10)
```

### 成员介绍

#### numerator和denominator
* 分子与分母

```
>>> import fractions
>>> fractions.Fraction(1/8.).numerator
1
>>> fractions.Fraction(.125).denominator
8
``` 

#### limit_denominator(max_denominator=1000000)
* 精度控制

```
>>> fractions.Fraction(math.pi).limit_denominator(1000000)
Fraction(3126535, 995207)
>>> fractions.Fraction(math.pi).limit_denominator(100)
Fraction(311, 99)
>>> fractions.Fraction(math.pi)
Fraction(884279719003555, 281474976710656)
```