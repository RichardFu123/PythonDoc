# Python的真值判定
> python3.7
> 文档：
> https://docs.python.org/3.7/library/stdtypes.html#truth-value-testing

--------
* python中有很多时候可以直接将对象用在if和while中.
* 但是在功能上,这些位置是需要通过Boolean来进行判断的.
* 这就牵扯到Python对于True和False的设计概念.
* **在默认状态下,python会认定你的对象恒为真直到对象的\_\_bool\_\_()方法返回false或者对象的\_\_len\_\_()返回0.**
* 包括但不限于以下状况:
	* None与False
	* 任何数学形式的0:0,0.0,0j,Decimal(0),Fraction(0,1)
	* 空队列/集合:'',(),[],{},set(),range(0)

--------
* 以下案例说明了:
	* 1.无\_\_len\_\_()与\_\_bool\_\_()状态下,python将对象恒判断为真.
	* 2,3.在有\_\_len\_\_()或\_\_bool\_\_()状态下,python根据其返回结果来判断真伪.
	* 4.1,4.2:在\_\_len\_\_()与\_\_bool\_\_()同时存在时,python只会承认\_\_bool\_\_()的结果,无视\_\_len\_\_()的结果.


```
# 1.在无__len__()与__bool__()状态下:

class test:
    def __init__(self,n):
        self.lis = []
        for i in range(n):
            self.lis.append(i)

    def print(self):
        try:
            print(self.lis.pop())
        except:
            print("empty list")

=================== RESTART: F:\PyWorkspace\booleanTest.py ===================
>>> t = test(9)
>>> while t:
	t.print()

	
8
7
6
5
4
3
2
1
0
empty list
empty list
empty list
empty list
...




# 2.在定义了__len__()的状态下:

class test:
    def __init__(self,n):
        self.lis = []
        for i in range(n):
            self.lis.append(i)

    def print(self):
        try:
            print(self.lis.pop())
        except:
            print("empty list")

    def __len__(self):
        return len(self.lis)
        
=================== RESTART: F:\PyWorkspace\booleanTest.py ===================
>>> t = test(10)
>>> while t:
	t.print()

	
9
8
7
6
5
4
3
2
1
0
>>> 

# 3.在定义了__bool__()的状态下:

class test:
    def __init__(self,n):
        self.flag = False
        self.lis = []
        for i in range(n):
            self.lis.append(i)
            self.flag = True

    def print(self):
        try:
            print(self.lis.pop())
        except:
            print("empty list")
            self.flag = False

    def __bool__(self):
        return self.flag


=================== RESTART: F:\PyWorkspace\booleanTest.py ===================
>>> t = test(5)
>>> while t:
	t.print()

	
4
3
2
1
0
empty list
>>> 

# 4.1在同时定义了__len__()与__bool__()的状态下:

class test:
    def __init__(self,n):
        self.flag = False
        self.lis = []
        for i in range(n):
            self.lis.append(i)
            self.flag = True

    def print(self):
        try:
            print(self.lis.pop())
        except:
            print("empty list")
            self.flag = False

    def __bool__(self):
        return self.flag

    def __len__(self):
        return len(self.lis)

=================== RESTART: F:\PyWorkspace\booleanTest.py ===================
>>> t = test(4)
>>> while t:
	t.print()

	
3
2
1
0
empty list
>>> 

# 4.2在同时定义了__len__()与__bool__()的状态下:

class test:
    def __init__(self,n):
        self.flag = False
        self.lis = []
        for i in range(n):
            self.lis.append(i)
            self.flag = True

    def print(self):
        try:
            print(self.lis.pop())
        except:
            print("empty list")
            self.flag = False

    def __bool__(self):
        return True

    def __len__(self):
        return len(self.lis)

=================== RESTART: F:\PyWorkspace\booleanTest.py ===================
>>> t = test(4)
>>> while t:
	t.print()

	
3
2
1
0
empty list
empty list
empty list
empty list
empty list
empty list
empty list
...
```