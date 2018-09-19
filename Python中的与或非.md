# Python中的与或非以及逻辑短路
> python3.7
> Shawn
> 文档：
> https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

## 与或非

* python中的与或非与java等静态有些许不一样.
* 受益于动态语言的特性,python中的与或非可以实现更多的操作:

```
>>> print(0 or [1,2,3])
[1, 2, 3]
>>> print(0 and [])
0
>>> print(set() or True)
True
```

* 由于python对于对象的布尔判断是基于对象的\_\_bool\_\_()方法或\_\_len\_\_()方法的,所以**或和与返回的其实是判断对象而不是布尔值!**
* 可以将与或非近似理解为下面的函数:

```
def BooleanNOT(x):
    # not x
    if x:
        return False
    else:
        return True


def BooleanOR(x, y):
    # x or y
    if not x:
        return y
    else:
        return x

def BooleanAND(x, y):
    # x and y
    if not x:
        return x
    else:
        return y

```

## 逻辑短路

* 由上一节,可以十分直观地了解到: 在逻辑判断中,并不是每一个判断对象都会被执行.
* 与运算的第一个对象值为false,则第二个对象会被略过.
* 或运算的第一个对象值为true,则第二个同样对象会被略过.
* 这种由于逻辑运算机制而导致的现象就叫做逻辑短路.

```
>>> def print_but_false():
		print("print but false")
		return False

>>> True or print_but_false()
True
>>> False and print_but_false()
False
>>> print_but_false() and True
print but false
False
>>> 
```