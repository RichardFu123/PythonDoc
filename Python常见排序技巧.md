# Python：如何排序
> python3.7
> 本文参考、翻译自Andrew Dalke and Raymond Hettinger的《Sorting HOW TO》（Release-0.1）
> 原文地址：
> https://docs.python.org/3/howto/sorting.html

* 就排序而言，Python中的list容器内置了sort()方法，可以原地排序。此外，也有内建方法sorted()可以用其他的iterable生成一个新的、排过序的list。

* 在此基础上，本文将介绍更灵活的、高级的排序技巧。

## 基本操作

* 说道排序，最简单最直观的概念就是：从小到大依次排开。
* 考虑到结果的使用情况，Python里直接提供了两种方法：内建的sorted()与list的sort()方法。
* 区别在于：
	* sorted()方法需要传入一个iterable而创建一个新的list。
	* list的sorted()方法可以不传入参数而直接使用，功能是对list本身进行排序而不产生新的list。
	* sorted()不光可以对list进行排序，只要是iterable都可以。
```
>>> list1=[6,3,5,1,2]
>>> list2=[2,3,5,1,8]
>>> list3=sorted(list1)
>>> list2.sort()
>>> list1
[6, 3, 5, 1, 2]
>>> list2
[1, 2, 3, 5, 8]
>>> list3
[1, 2, 3, 5, 6]
```
```
>>> dict1={1:'Shawn',2:'sort',3:'sorted'}
>>> sorted(dict1)
[1, 2, 3]
```

## 扩展功能

* list.sort()与sorted()其实都有一个可选参数key，其作用就是调整排序的逻辑。
```
>>> sorted("This is a test string from Shawn".split(), key=str.lower)
['a', 'from', 'is', 'Shawn', 'string', 'test', 'This']
>>> sorted("This is a test string from Shawn".split())
['Shawn', 'This', 'a', 'from', 'is', 'string', 'test']
```

* key参数需要是一个方法，用于调整实际所需排序的逻辑。
* 就上面的例子而言，第一个sorted进行排序之前会对每一个单词调用str的lower方法，相当于对这些单词的小写形式进行了排序。
* 这就使得sort()与sorted()的用途更加广阔，比如二维数组的排序：
```
>>> list2D=[[1,9,'doge'],[2,8,'bug'],[3,7,'dummy']]
>>> sorted(list2D,key=lambda element:element[1])
[[3, 7, 'dummy'], [2, 8, 'bug'], [1, 9, 'doge']]
```
	* 这里就定义了一个匿名函数，其作用是返回所传入参数中索引为1的元素。
	* 也就是说，在这里排序的实际上是`[9,8,7]`
* 同样，对于类来讲，调用合适的内部方法也一样可以进行排序了：
```
>>> class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age
	def __repr__(self):
		return repr((self.name, self.grade, self.age))
>>> student_objects = [
	Student('john', 'A', 15),
	Student('jane', 'B', 12),
	Student('dave', 'B', 10),
	]
>>> sorted(student_objects, key=lambda student: student.age)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## 与operator模块的结合

* 同样的，operator的模块中的itemgetter()，attrgetter()以及methodcaller()也都可以用于key参数。
* 这三者的介绍详见[operator模块](https://blog.csdn.net/weixin_41084236/article/details/81509339)。
```
>>> from operator import itemgetter, attrgetter
>>> sorted(list2D, key=itemgetter(2))
[[2, 8, 'bug'], [1, 9, 'doge'], [3, 7, 'dummy']]
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

* 用operator模块也支持多层次的排序，比如：先成绩再年龄：
```
>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

* 或者先第二项而后第三项：
```
>>> sorted(list2D, key=itemgetter(1,2))
[[3, 7, 'dummy'], [2, 8, 'bug'], [1, 9, 'doge']]
```

## 正序与倒序

* list.sort()与sorted()还有另一个可选参数：reverse。
* 其作用如其名，默认为False。
* 将其指定为True则输出倒序。
```
>>> sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

## 排序稳定性以及复杂排序

* Python中排序的一个很重要的性质就是：当两个值有相同的key的时候，其在排序后的顺序与输入顺序一致。
```
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data, key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
```
	* 在这里，'blue'内部的相对顺序保持了一致，'red'也一样。


* 这就让我们可以逐次叠加，实现更复杂的排序。
* 比如：在成绩从第到高的情况下，进行年龄从小到大的排序：
```
>>> s = sorted(student_objects, key=attrgetter('grade'), reverse=True)
>>> s
[('jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]
>>> sorted(s, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## 用朴素方法实现指定要素排序

* 整个流程分三步：
	* 将每个元素中所指定的子元素提到首位。
	* 排序。
	* 恢复元素内的顺序。

```
>>> decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
>>> decorated.sort()
>>> [student for grade, i, student in decorated]
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

* 以上用传统方法实现了按成绩排序。
* 在元组排序中，默认按元组第一项进行排序，若相同则比较第二项，依次往后。

## Python2到Python3的解决方案

* Python2中所用的排序中，有另一个重要参数cmp，但是在Python3中已经不存在了。
* 比如在Py2中，正序和倒序排序可以以下表达：

```
>>> def numeric_compare(x, y):
...     return x - y
>>> sorted([5, 2, 4, 1, 3], cmp=numeric_compare) 
[1, 2, 3, 4, 5]

>>> def reverse_numeric(x, y):
...     return y - x
>>> sorted([5, 2, 4, 1, 3], cmp=reverse_numeric) 
[5, 4, 3, 2, 1]
```

在Py3中，则需要调用functools中的cmp_to_key方法来进行移植：
```
>>> import functools
>>> def reverse_numeric(x, y):
	return y - x

>>> sorted([5, 2, 4, 1, 3], key=functools.cmp_to_key(reverse_numeric))
[5, 4, 3, 2, 1]
```
```
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
```

## 杂项
* 用locale.strxfrm()作为key方法，或者用locale.strcoll()作为比较方法可以解决一些特定地区语言的字符串排序问题。
* reverse()方法一样有着排序稳定性。
* 排序方法在实现的时候会优先调用被排序类的__it__()方法，所以如果不想每次排序都指定key方法或者其他参数，可以考虑直接改写__it__()方法。
	* 这里直接通过重写__it__()方法达到了默认对比属性为年龄的效果。
```
>>> Student.__lt__ = lambda self, other: self.age < other.age
>>> sorted(student_objects)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

* 之前说过，key方法所起的作用仅仅是将待排序元素逐个进行加工提取，所以key方法其实并不依赖待排序元素：
	* 这里通过待排序元素访问获取外部储存的数据，进行了排序。
```
>>> students = ['dave', 'john', 'jane']
>>> newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
>>> sorted(students, key=newgrades.__getitem__)
['jane', 'dave', 'john']
```