# 迭代器模块：itertools
> python3.7
> 文档：
> https://docs.python.org/3/library/itertools.html

* itertools中有许多有意思的功能，使用得当可以节约大量生命。

### 无限迭代器

#### count()

    itertools.count(start=0,step=1)

* 返回以start为开头，步长step的值。

```
>>> for i in itertools.count():
	print(i)
	
0
1
2
3
4
...
```

#### cycle()：复读机一号


    itertools.cycle(iterable)

* 保存对象的副本，并无限重复返回每一个元素。

```
>>> for i in itertools.cycle([2,3,4,5]):
	print(i)

2
3
4
5
2
3
4
5
2
...
```

#### repeat()：复读机二号


    itertools.repeat(object[,times])

* 重复返回对象[次]。

```
>>> for i in itertools.repeat('雪碧'):
	print(i)

雪碧
雪碧
雪碧
雪碧
雪碧
...
```

### 终止于最短输入的迭代器

#### accumulate()

    itertools.accumulate(iterable[, func])

* 对iterable对象内的每个元素依次做func运算，更新并输出。
* func要求为二目运算，详见operator模块

```
>>> for i in itertools.accumulate([1,2,3,4],operator.add):
	print(i)

	
1
3
6
10
>>> for i in itertools.accumulate([1,2,3,4],operator.mul):
	print(i)

	
1
2
6
24
```

#### chain()

    itertools.chain(*iterables)

* 将所有输入拼接输出。

```
>>> a='把你的心'
>>> b=' 我的心'
>>> c=' 串一串'
>>> for i in itertools.chain(a,b,c):
	print(i)

	
把
你
的
心
 
我
的
心
 
串
一
串
```

#### chain.from_iterable()

    chain.from_iterable(iterable)

* 将单个iterable中的所有元素拼接输出。

```
>>> d=['串一株幸运草',' 串一个同心圆']
>>> for i in itertools.chain.from_iterable(d):
	print(i)

	
串
一
株
幸
运
草
 
串
一
个
同
心
圆
```

#### compress()
    itertools.compress(data,selectors)

* 返回data中对应selectors为True的元素。
* 相当于把selectors当做滤镜套在了data上。

```
>>> selec=[True,False,42,0,-42,'shuang']
>>> items=['mole','xiangxiangji','tazhenmei','wodene','migang','shuangsile']
>>> for i in itertools.compress(items,selec):
	print(i)

mole
tazhenmei
migang
shuangsile
```

#### dropwhile()

    itertools.dropwhile(predicate, iterable)

* 从头开始，干掉不符合的元素，直到第一个正确元素。

```
>>> for i in itertools.dropwhile(lambda x:x<7,[1,2,3,6,7,8,2,4,5,9]):
	print(i)

	
7
8
2
4
5
9
```

#### filterfalse()

    itertools.filterfalse(predicate, iterable)

* 输出为错的要素：

```
>>> for i in itertools.filterfalse(lambda x:x=='moyu',['moyu','jinye']):
	print(i)
jinye
```

#### groupby()

    itertools.groupby(iterable, key=None)

* 将iterable同要素聚合输出：

```
>>> for k,g in itertools.groupby('aaAAaBBBCCCCC'):
	print(k)
	print(list(g))

	
a
['a', 'a']
A
['A', 'A']
a
['a']
B
['B', 'B', 'B']
C
['C', 'C', 'C', 'C', 'C']
```

#### islice()

    itertools.islice(iterable, stop)
    itertools.islice(iterable, start, stop[, step])

* 切片操作的迭代器版本

```
>>> for i in itertools.islice('fengliutitangShawn',0,None,2):
	print(i)

	
f
n
l
u
i
a
g
h
w
```

#### starmap()

    itertools.starmap(function, iterable)

* map的迭代器版本

```
>>> for i in itertools.starmap(operator.add,[(1,2),(3,4),(5,6)]):
	print(i)

	
3
7
11
```

#### takewhile()

    itertools.takewhile(predicate, iterable)

* 与filterfalse()的判断条件相反。

```
>>> for i in itertools.takewhile(lambda x:x=='moyu',['moyu','jinye']):
	print(i)

	
moyu
```

#### tee()

    itertools.tee(iterable, n=2)

* 创建n个与iterable相同的独立迭代器。

```
>>> for i in itertools.tee([1,2,3,4,5,6]):
	for j in i:
		print(j)

		
1
2
3
4
5
6
1
2
3
4
5
6
```

#### zip_longest()

    itertools.zip_longest(*iterables[,fillvalue=none])

* 用最长序列来zip，短序列填充fillvalue

```
>>> for i in itertools.zip_longest('Twilight Sparkle','Rainbow Dash','Fluttershy','Apple Bloom',fillvalue='Biu'):
	print(i)

	
('T', 'R', 'F', 'A')
('w', 'a', 'l', 'p')
('i', 'i', 'u', 'p')
('l', 'n', 't', 'l')
('i', 'b', 't', 'e')
('g', 'o', 'e', ' ')
('h', 'w', 'r', 'B')
('t', ' ', 's', 'l')
(' ', 'D', 'h', 'o')
('S', 'a', 'y', 'o')
('p', 's', 'Biu', 'm')
('a', 'h', 'Biu', 'Biu')
('r', 'Biu', 'Biu', 'Biu')
('k', 'Biu', 'Biu', 'Biu')
('l', 'Biu', 'Biu', 'Biu')
('e', 'Biu', 'Biu', 'Biu')
```

### 组合生成器

#### product()

    itertools.product(*iterables[,repeat=1])

* 对*iterables进行笛卡尔积运算。

```
>>> for i in itertools.product('Tom','Jerry',repeat=1):
	print(i)

('T', 'J')
('T', 'e')
('T', 'r')
('T', 'r')
('T', 'y')
('o', 'J')
('o', 'e')
('o', 'r')
('o', 'r')
('o', 'y')
('m', 'J')
('m', 'e')
('m', 'r')
('m', 'r')
('m', 'y')
```


#### permutations()
    itertools.permutations(iterable[,r])

* 返回连续长度为r（默认为最大长度）的迭代对象。

```
import itertools

digi=[1,2,3]
for item in itertools.permutations(digi,2):
    print(item)
for item in itertools.permutations(range(3)):
    print(item)

(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)
```


#### combinations()和combinations_with_replacement()


    itertools.combinations(iterable, r)
    itertools.combinations_with_replacement(iterable, r)

* combinataions与permutations类似，但由前到后返回不重复（索引组合）的迭代。
* combinations_with_replacement与combinataions类似，但是将自身索引也作为一次对象。

```
import itertools

digi=[1,2,3]
for item in itertools.combinations(digi,2):
    print(item)
print ("\n")
for item in itertools.combinations(range(3),2):
    print (item)

(1, 2)
(1, 3)
(2, 3)

(0, 1)
(0, 2)
(1, 2)

import itertools

digi=[1,2,3]
for item in itertools.combinations_with_replacement(digi,2):
    print(item)

(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)
```