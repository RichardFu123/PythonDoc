# 拷贝模块copy
> python3.7
> 文档：
> https://docs.python.org/3/library/copy.html

* Python的拷贝模块提供的功能不是很多,但不代表不重要.

## copy

    copy.copy(x)

* 返回一个浅拷贝.

## deepcopy

    copy.deepcopy(x)

* 返回一个深拷贝.

## 拷贝详解
* 拷贝操作直接影响到程序能否正确按照设计思路运行.
* 不正确的拷贝往往不报错,而这也是很多bug的原因.
* 这里直接提供一个直观的例子:

```
import copy
a = [1,2,3,4,['a','b']]

b = a                   # 赋值
c = a[:]                # 浅拷贝
d = copy.copy(a)        # 浅拷贝
e = copy.deepcopy(a)    # 深拷贝

a.append(5)
a[4].append('c')

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print('e=',e)

============ RESTART: F:\PyWorkspace\Python100\100examples\007.py ============
a= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c= [1, 2, 3, 4, ['a', 'b', 'c']]
d= [1, 2, 3, 4, ['a', 'b', 'c']]
e= [1, 2, 3, 4, ['a', 'b']]
```

* 毫不意外,Python中的直接赋值也只是传递对象,好比隔壁老王和你的关系.
* 对于copy操作来说,拷贝只进行了一层,之后的引用关系依然保留.
* 最彻底的拷贝操作是deepcopy.其功能与名字一样,会递归深入你的对象,将其里里外外每个层次都拷贝一份.

```
class deepdark():
    def __init__(self):
        self.fantasy=list()
        self.fantasy.append('oh')
    def banana(self):
        print(self.fantasy)
    def boyNextDoor(self):
        self.fantasy.append('my shoulder')

====================== RESTART: F:\PyWorkspace\blank.py ======================

>>> import copy
>>> a=deepdark()
>>> b=[1,a]
>>> c=copy.copy(b)
>>> d=copy.deepcopy(b)

>>> a.boyNextDoor()
>>> a.banana()
['oh', 'my shoulder']
>>> b[1].banana()
['oh', 'my shoulder']
>>> c[1].banana()
['oh', 'my shoulder']
>>> d[1].banana()
['oh']
```

* 这里可以很容易发现,deepcopy对于类的拷贝是直接生成一个值相同的新对象.

```
>>> e=copy.copy(a)
>>> a.boyNextDoor()
>>> a.banana()
['oh', 'my shoulder', 'my shoulder']
>>> e.banana()
['oh', 'my shoulder', 'my shoulder']

>>> e.boyNextDoor()
>>> e.banana()
['oh', 'my shoulder', 'my shoulder', 'my shoulder']
>>> a.banana()
['oh', 'my shoulder', 'my shoulder', 'my shoulder']

>>> f=copy.deepcopy(a)
>>> a.boyNextDoor()
>>> a.banana()
['oh', 'my shoulder', 'my shoulder', 'my shoulder', 'my shoulder']
>>> f.banana()
['oh', 'my shoulder', 'my shoulder', 'my shoulder']
```

* 所以,对于一个类的话,copy只是生成一个引用,而deepcopy才是进行复制.