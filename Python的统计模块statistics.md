# 统计模块statistics
> python3.7
> https://docs.python.org/3/library/statistics.html

## 方法介绍

#### statistics.mean(data)
* 就是平均值
* 支持的输入非常多，包括fractions模块和decimal模块

```
>>> mean([1, 2, 3, 4, 4])
2.8
>>> mean([-1.0, 2.5, 3.25, 5.75])
2.625

>>> from fractions import Fraction as F
>>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
Fraction(13, 21)

>>> from decimal import Decimal as D
>>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
Decimal('0.5625')
```

#### statistics.harmonic_mean(data)
* 调和平均数

```
>>> from statistics import *
>>> harmonic_mean([1,2,3])
1.6363636363636365
>>> 1/sum([1./1,1./2,1./3])*3
1.6363636363636367
```

#### statistics.median(data)
* 中值

```
>>> median([1, 3, 5])
3
>>> median([1, 3, 5, 7])
4.0
```

#### statistics.median_low(data)
* 小中值
* 若中值有两个，则选择较小的那个

```
>>> median_low([1, 3, 5])
3
>>> median_low([1, 3, 5, 7])
3
```

#### statistics.median_high(data)
* 大中值
* 若中值有两个，则选择较大的那个

```
>>> median_high([1, 3, 5])
3
>>> median_high([1, 3, 5, 7])
5
```

#### statistics.median_grouped(data, interval=1)
* 用组距式来求中位数
* 公式：`中位数=中位数所在组下限+{[(样本总数/2-到中位数所在组下限的累加次数)/中位数所在组的次数]*中位数的组距}`
* 参数说明：
	* interval：组距，例子：
		* 如果组距为1，则1在组0.5~1.5；
		* 如果组距为2，则3在组2~4

```
>>> median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5])
3.7
>>> median_grouped([1, 3, 3, 5, 7], interval=1)
3.25
>>> median_grouped([1, 3, 3, 5, 7], interval=2)
3.5
```
* 示例说明：
	* [1, 2, 2, 3, 4, 4, 4, 4, 4, 5]中位数在4这个分组里面
		* 默认组距为1
		* 所在分组的下限为3.5
		* 样本总数为10
		* 4分组里有5个数
		* 小于3.5的有4个数
		* 所以中位数为：3.5+(10/2-4)/5*1=3.5+1/5=3.7
	* [1, 3, 3, 5, 7], interval=2，中位数在3分组里
		* 组距为2
		* 所在分组下限为2
		* 总数为5
		* 3分组里有2个数
		* 小于2的有1个数
		* 中位数：2+(5/2-1)/2*2=2+1.5=3.5

#### statistics.mode(data)
* 众数

```
>>> mode([1, 1, 2, 3, 3, 3, 3, 4])
3
>>> mode(["red", "blue", "blue", "red", "green", "red", "red"])
'red'
```

#### statistics.pstdev(data, mu=None)
* 总体标准差
* 设定已知均值mu可以减少计算量

```
>>> pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
0.986893273527251
```

#### statistics.pvariance(data, mu=None)
* 总体方差
* 设定已知均值mu可以减少计算量

```
>>> data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
>>> pvariance(data)
1.25
```

#### statistics.stdev(data, xbar=None)
* 样本标准差

```
>>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
1.0810874155219827
```

#### statistics.variance(data, xbar=None)
* 样本方差

```
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> variance(data)
1.3720238095238095
```