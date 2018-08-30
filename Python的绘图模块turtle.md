# 小海龟历险记
> Shawn 
> python3.7
> 文档：
> https://docs.python.org/3/library/turtle.html

* 想象一下,把一个小海龟扔到沙滩上.小海龟爬啊爬,沙滩上留下来一道道痕迹,这就是turtle模块.

## 小海龟的动作

### 爬行

#### 前进:forward/fd

```
turtle.forward(distance)
turtle.fd(distance)
Parameters:	distance – a number (integer or float)
```

* 小海龟朝当前方向向前爬行.

#### 后退:back/bk/backward

```
turtle.back(distance)
turtle.bk(distance)
turtle.backward(distance)
Parameters:	distance – a number (integer or float)
```

* 小海龟向后爬行.

#### 右拐(顺时针转):right/rt

```
turtle.right(angle)
turtle.rt(angle)
Parameters:	distance – a number (integer or float)
```
* 小海龟顺指针转向.

#### 左拐(逆时针转):left/lt

```
turtle.left(angle)
turtle.lt(angle)
Parameters:	angle – a number (integer or float)
```

* 小海龟逆时针转向.

#### 爬到指定位置:goto/setpos/setposition

```
turtle.goto(x, y=None)
turtle.setpos(x, y=None)
turtle.setposition(x, y=None)
Parameters:	
x – a number or a pair/vector of numbers
y – a number or None
```

* 小海龟爬到指定的坐标位置.

#### x轴上移动:setx

```
turtle.setx(x)
Parameters:	x – a number (integer or float)
```

* 小海龟横向爬行.

#### y轴上移动:sety

```
turtle.sety(y)
Parameters:	y – a number (integer or float)
```

* 小海龟纵向爬行.

#### 转向指定方向:setheading/seth

```
turtle.setheading(to_angle)
turtle.seth(to_angle)
Parameters:	to_angle – a number (integer or float)
```

* 小海龟朝向指定方向.
* **注意,默认的方向可能有所不同:**

|standard mode|logo mode|
|:-|:-|
|0 - east|0 - north|
|90 - north|90 - east|
|180 - west|180 - south|
|270 - south|270 - west|

#### 回家:home

```
turtle.home()
```

* 小海龟回到图像原点(0,0),**并朝向默认初始方向**.

#### 画圆:circle

```
turtle.circle(radius, extent=None, steps=None)
Parameters:	
radius – a number
extent – a number (or None)
steps – an integer (or None)
```

* 小海龟从当前位置开始向前画半径为radius,角度为extent的圆弧.
* radius为正,则逆时针,反之顺时针.
* 在turtle里,本质上,画圆弧相当于画n段直线.
* 用steps可以指定n的数量.换而言之,可以用于实现一些多边形.

#### 画点:dot

```
turtle.dot(size=None, *color)
Parameters:	
size – an integer >= 1 (if given)
color – a colorstring or a numeric color tuple
```

* 在当前位置画一个直径为size,颜色为color的点.
* 如果没有指定size,会默认选择max(当前笔粗+4,当前笔粗*2)

#### 海龟分身:stamp

```
turtle.stamp()
```

* 在当前位置保存一个一模一样小海龟幻象,并返回这个幻象的id.

#### 分身解除:clearstamp

```
turtle.clearstamp(stampid)
Parameters:	stampid – an integer, must be return value of previous stamp() call
```

* 根据id解除海龟分身.

#### 批量分身解除:clearstamps

```
turtle.clearstamps(n=None)
Parameters:	n – an integer (or None)
```

* 批量解除分身.
* 默认全部,若n为正则解除最早n个,为负责解除最晚n个.

#### 时光回溯:undo

```
turtle.undo()
```

* 每执行一次可以回到上一步的状态.

#### 调速:speed

```
turtle.speed(speed=None)
Parameters:	speed – an integer in the range 0..10 or a speedstring (see below)
```

* “fastest”: 0
* “fast”: 10
* “normal”: 6
* “slow”: 3
* “slowest”: 1

* 调节小海龟爬行以及转向的速度.
* 从1到10逐步加快,也可以设定为最快:0.
* **注意:小于等于0.5或者大于10都会被直接设定为0**

### 海龟状态查询

#### 海龟位置:position/pos

```
turtle.position()
turtle.pos()
```

* 返回小海龟当前的位置.

#### 小海龟的头部与目标间的角度:towards

```
turtle.towards(x, y=None)
Parameters:	
x – a number or a pair/vector of numbers or a turtle instance
y – a number if x is a number, else None
```

* 返回小海龟当前方向与指定坐标(或者另一个海龟实体)连线的夹角.

#### x坐标查询:xcor

```
turtle.xcor()
```

* 返回x坐标.

#### y坐标查询:ycor

```
turtle.ycor()
```

* 返回y坐标.

#### 当前方向:heading

```
turtle.heading()
```

* 返回小海龟当前方向.

#### 距离查询:distance

```
turtle.distance(x, y=None)
Parameters:	
x – a number or a pair/vector of numbers or a turtle instance
y – a number if x is a number, else None
```

* 返回小海龟与指定坐标(或者另一个海龟实体)间的距离.

### 定制规则

#### 一圈有多少度:degrees

```
turtle.degrees(fullcircle=360.0)
Parameters:	fullcircle – a number
```

* 设定一圈有多少度.如果你填400,那在小海龟的世界里一圈会被划分成400份而不是360份.

#### 用弧度:radians

```
turtle.radians()
```

* 设定用弧度而不是角度.

### 画笔

* 好吧,可爱的小海龟现在终于变成画笔了.

#### 下笔(肚皮贴地):pendown/pd/down

```
turtle.pendown()
turtle.pd()
turtle.down()
```

* 开始画出移动轨迹.

#### 抬笔(肚皮离地):penup/pu/up

```
turtle.penup()
turtle.pu()
turtle.up()
```

* 移动时不画线了.

#### 笔粗:pensize/width

```
turtle.pensize(width=None)
turtle.width(width=None)
Parameters:	width – a positive number
```

* 设定画笔的粗细.
* 如果无参数,返回当前笔粗.

#### 画笔(海龟)状态总控:pen

```
turtle.pen(pen=None, **pendict)
Parameters:	
pen – a dictionary with some or all of the below listed keys
pendict – one or more keyword-arguments with the below listed keys as keywords
```

* 可以调节\查询当前画笔的状态.
	* “shown”: True/False
	* “pendown”: True/False
	* “pencolor”: color-string or color-tuple
	* “fillcolor”: color-string or color-tuple
	* “pensize”: positive number
	* “speed”: number in range 0..10
	* “resizemode”: “auto” or “user” or “noresize”
	* “stretchfactor”: (positive number, positive number)
	* “outline”: positive number
	* “tilt”: number

#### 是否在画:isdown

```
turtle.isdown()
```

* 返回当前是否是pendown状态.

### 颜色控制

#### 画笔颜色:pencolor

```
turtle.pencolor(*args)
```

* 设定画笔颜色:
	* 无参数:返回当前画笔颜色.
	* 颜色名字符串或TKcolor字符串:设定颜色
		* "red", "yellow", "#33cc8c"
	* rgb元组或rgb单值:设定颜色
		* (0.2, 0.8, 0.55),(51.0, 204.0, 140.0)
		* 255模式或者1.0模式由colormode()设定:
			* colormode(255)
			* colormode(1)

#### 填充颜色: fillcolor

```
turtle.fillcolor(*args)
```

* 设定填充颜色,方法同pencolor

#### 颜色总控:color

```
turtle.color(*args)
```

* 同时查询\设定画笔颜色与填充颜色.
* 第一组参数为画笔颜色.
* 第二组参数为填充颜色.

### 填充控制

#### 填充状态:filling

```
turtle.filling()
```

* 返回填充状态.

#### 开始填充:begin_fill

```
turtle.begin_fill()
```

* 开始计算填充图形.

#### 正式填充:end_fill

```
turtle.end_fill()
```

* 计算从上一个begin_fill开始的图形,并进行填充.

### 更多骚操作

#### 初始化:reset

```
turtle.reset()
```

* 清空沙滩并且复原小海龟.

#### 清理沙滩:clear

```
turtle.clear()
```

* 将沙滩上的图形清空.

#### 写字:write

```
turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
Parameters:	
arg – object to be written to the TurtleScreen
move – True/False
align – one of the strings “left”, “center” or right”
font – a triple (fontname, fontsize, fonttype)
```

* 按照参数将arg写在沙滩上.

### 其他海龟参数

#### 海龟可见

##### 隐藏海龟:hideturtle/ht

```
turtle.hideturtle()
turtle.ht()
```

* 隐藏海龟

##### 显示海龟:showturtle/st

```
turtle.showturtle()
turtle.st()
```

* 显示海龟

##### 海龟可见状态查询:isvisible

```
turtle.isvisible()
```

* 查询海龟可见状态.

#### 海龟外观

##### 海龟外形:shape

```
turtle.shape(name=None)
Parameters:	name – a string which is a valid shapename
```

*  “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
*  小海龟可以变身成圆圈\三角等

##### 海龟大小缩放:resizemode

```
turtle.resizemode(rmode=None)
Parameters:	rmode – one of the strings “auto”, “user”, “noresize”
```

* 设定海龟大小缩放模式:
	* “auto”: adapts the appearance of the turtle corresponding to the value of pensize.
	* “user”: adapts the appearance of the turtle according to the values of stretchfactor and outlinewidth (outline), which are set by shapesize().
	* “noresize”: no adaption of the turtle’s appearance takes place.

##### 海龟大小详细设置:shapesize/turtlesize

```
turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
turtle.turtlesize(stretch_wid=None, stretch_len=None, outline=None)
Parameters:	
stretch_wid – positive number
stretch_len – positive number
outline – positive number
```

* 在resizemode为'user'时起效.

##### 海龟剪切系数:shearfactor

```
turtle.shearfactor(shear=None)
Parameters:	shear – number (optional)
```

* 设定海龟外观的剪切形变系数.
* 不改变朝向.

##### 海龟外形旋转:tilt/settiltangle

```
turtle.tilt(angle)
turtle.settiltangle(angle)
Parameters:	angle – a number
```

* 旋转海龟外形.
* 不同的是tilt会根据当前angle做出调整.
* 而settiltangle为绝对角度.

##### 海龟外形角度查询:tiltangle

```
turtle.tiltangle(angle=None)
Parameters:	angle – a number (optional)
```

* 返回当前外观角度.
* 如果有参数,效果同settiltangle.

##### 海龟外形总控:shapetransform

```
turtle.shapetransform(t11=None, t12=None, t21=None, t22=None)
Parameters:	
t11 – a number (optional)
t12 – a number (optional)
t21 – a number (optional)
t12 – a number (optional)
```

* 返回(设置)当前海龟外形变形参数(参照shapesize\shearfactor\settiltangle).

##### 海龟外观获取:get_shapepoly

```
turtle.get_shapepoly()
```

* 获取当前海龟外形的图形坐标元组.

### 事件监听器

#### 监听器:listen

```
turtle.listen(xdummy=None, ydummy=None)
Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to be able to pass listen() to the onclick method.
```

* 在屏幕上设置监听区域.

#### 监听鼠标按键按下:onclick

```
turtle.onclick(fun, btn=1, add=None)
Parameters:	
fun – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
num – number of the mouse-button, defaults to 1 (left mouse button)
add – True or False – if True, a new binding will be added, otherwise it will replace a former binding
```

* 按下鼠标时,执行绑定的操作.

#### 监听鼠标按键抬起:onrelease

```
turtle.onrelease(fun, btn=1, add=None)
Parameters:	
fun – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
num – number of the mouse-button, defaults to 1 (left mouse button)
add – True or False – if True, a new binding will be added, otherwise it will replace a former binding
```

* 抬起鼠标按键时,执行绑定的操作.

#### 监听鼠标按键拖动:ondrag

```
turtle.ondrag(fun, btn=1, add=None)
Parameters:	
fun – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
num – number of the mouse-button, defaults to 1 (left mouse button)
add – True or False – if True, a new binding will be added, otherwise it will replace a former binding
```

* 拖动鼠标按键时,执行绑定的操作.

#### 监听键盘按键:onkey/onkeyrelease/onkeypress

```
turtle.onkey(fun, key)
turtle.onkeyrelease(fun, key)
turtle.onkeypress(fun, key=None)
Parameters:	
fun – a function with no arguments or None
key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
```

* 按下\释放键盘相应按键时,执行操作.

#### 定时操作:ontimer

```
turtle.ontimer(fun, t=0)
Parameters:	
fun – a function with no arguments
t – a number >= 0
```

* 设定计时器,计时t毫秒后执行fun.

#### 时间循环:mainloop/done

```
turtle.mainloop()
turtle.done()
Starts event loop - calling Tkinter’s mainloop function. Must be the last statement in a turtle graphics program. Must not be used if a script is run from within IDLE in -n mode (No subprocess) - for interactive use of turtle graphics.
```

### 更多海龟操作

#### 开始记录多边形:begin_poly

```
turtle.begin_poly()
```

* 开始记录多边形,当前位置为第一个顶点.

#### 结束记录多边形:end_poly

```
turtle.end_poly()
```

* 结束记录多边形,当前位置为最后一个顶点.

#### 获取记录到的多边形:get_poly

```
turtle.get_poly()
```

* 获取最后一次记录到的多边形.

#### 克隆海龟:clone

```
turtle.clone()
```

* 创建并且返回一个当前海龟一模一样的克隆.

#### 查询海龟:getturtle/getpen

```
turtle.getturtle()
turtle.getpen()
```

* 返回海龟自己.

#### 查询屏幕:getscreen

```
turtle.getscreen()
```

* 返回海龟所在的沙滩,能用于调用其方法.

#### 设定undobuffer:setundobuffer

```
turtle.setundobuffer(size)
Parameters:	size – an integer or None
```

* 设定一个undobuffer,记录最多size步可以由undo反悔的海龟操作.
* 如果size为None,则关闭这个buffer.

#### 查询undobuffer:undobufferentries

```
turtle.undobufferentries()
```

* 返回undobuffer中现在有多少步.

## Screen/TurtleScreen操作

### 窗口控制

#### 背景色:bgcolor

```
turtle.bgcolor(*args)
Parameters:	args – a color string or three numbers in the range 0..colormode or a 3-tuple of such numbers
```

* 改变屏幕背景色(无参数则返回当前背景色.)

#### 背景图:bgpic

```
turtle.bgpic(picname=None)
Parameters:	picname – a string, name of a gif-file or "nopic", or None
```

* 设定或返回背景图,picname可以是文件名,如果为'nopic'则删除背景图.

#### 窗口size:screensize

```
turtle.screensize(canvwidth=None, canvheight=None, bg=None)
Parameters:	
canvwidth – positive integer, new width of canvas in pixels
canvheight – positive integer, new height of canvas in pixels
bg – colorstring or color-tuple, new background color
```

* 设定窗口宽\高\背景色.

#### world坐标:setworldcoordinates

```
turtle.setworldcoordinates(llx, lly, urx, ury)
Parameters:	
llx – a number, x-coordinate of lower left corner of canvas
lly – a number, y-coordinate of lower left corner of canvas
urx – a number, x-coordinate of upper right corner of canvas
ury – a number, y-coordinate of upper right corner of canvas
```

* 通过左下\右上两个点的坐标来设定world坐标系统,并切换到world模式(非world模式会reset).
* 如果已经是world模式,则所有的绘制会在新坐标下重绘.

### 动画操作

#### 延迟:delay

```
turtle.delay(delay=None)
Parameters:	delay – positive integer
```

* 设置绘画延迟时间(毫秒)

#### 快速绘图:tracer/update

```
turtle.tracer(n=None, delay=None)
Parameters:	
n – nonnegative integer
delay – nonnegative integer
turtle.update()
```

* tracer:关掉\开启绘图动画.n:每n次屏幕更新显示一次,delay:每次延时.
* update:屏幕更新.

### 输入操作

#### 弹出文本输入框:textinput

```
turtle.textinput(title, prompt)
Parameters:	
title – string
prompt – string
```

* 弹出一个文本输入框,并返回输入的字符串.

#### 弹出数字输入框:numinput

```
turtle.numinput(title, prompt, default=None, minval=None, maxval=None)
Parameters:	
title – string
prompt – string
default – number (optional)
minval – number (optional)
maxval – number (optional)
```

* 弹出一个数字输入框,并返回输入的数字.

### 模式设定

#### 绘画模式:mode

```
turtle.mode(mode=None)
Parameters:	mode – one of the strings “standard”, “logo” or “world”
```

* 设定或返回绘画模式.

|Mode|Initial turtle heading|positive angles|
|:-|:-|:-|
|“standard”|to the right (east)|counterclockwise|
|“logo”|upward (north)|clockwise|

#### 颜色模式:colormode

```
turtle.colormode(cmode=None)
Parameters:	cmode – one of the values 1.0 or 255
```

* 设定或返回当前颜色模式.

#### 查询画布:getcanvas

```
turtle.getcanvas()
```

* 返回当前画布.

#### 查询图形:getshapes

```
turtle.getshapes()
```

* 返回当前所有可用的海龟图形的名称列表

#### 注册新图形:register_shape/addshape

```
turtle.register_shape(name, shape=None)
turtle.addshape(name, shape=None)
```

* 注册一个新的图形.

#### 查询海龟:turtles

```
turtle.turtles()
```

* 返回当前屏幕上所有的海龟.

#### 查询屏幕尺寸:window_height/window_width

```
turtle.window_height()
turtle.window_width()
```

* 返回当前屏幕高/宽.

### 屏幕特有操作(非继承自TurtleScreen)

#### 关闭海龟绘图窗口:bye

```
turtle.bye()
```

#### 点击鼠标后关闭:exitonclick

```
turtle.exitonclick()
```

* 点击鼠标后关闭窗口.

#### 屏幕设定:setup

```
turtle.setup(width=_CFG["width"], height=_CFG["height"], startx=_CFG["leftright"], starty=_CFG["topbottom"])
Parameters:	
width – if an integer, a size in pixels, if a float, a fraction of the screen; default is 50% of screen
height – if an integer, the height in pixels, if a float, a fraction of the screen; default is 75% of screen
startx – if positive, starting position in pixels from the left edge of the screen, if negative from the right edge, if None, center window horizontally
starty – if positive, starting position in pixels from the top edge of the screen, if negative from the bottom edge, if None, center window vertically
```

* 设定屏幕的size以及位置.

#### 屏幕标题:title

```
turtle.title(titlestring)
Parameters:	titlestring – a string that is shown in the titlebar of the turtle graphics window
```

* 设定屏幕标题.

### 公共类

#### 造龟:RawTurtle/RawPen

```
class turtle.RawTurtle(canvas)
class turtle.RawPen(canvas)
Parameters:	canvas – a tkinter.Canvas, a ScrolledCanvas or a TurtleScreen
```

* 在给定画布上造一个龟.

#### 默认造龟:Turtle

```
class turtle.Turtle
```

* RawTurtle的子类,在默认屏幕上造龟.

#### 海龟屏:TurtleScreen

```
class turtle.TurtleScreen(cv)
Parameters:	cv – a tkinter.Canvas
```

* 提供一个海龟屏.

#### 屏幕:Screen

```
class turtle.Screen
```

* 海龟屏的子类,添加了上一节里的新功能(bye/title等)

#### 卷屏:ScrolledCanvas

```
class turtle.ScrolledCanvas(master)
Parameters:	master – some Tkinter widget to contain the ScrolledCanvas, i.e. a Tkinter-canvas with scrollbars added
Used by class Screen, which thus automatically provides a ScrolledCanvas as playground for the turtles.
```

#### 图形类:Shape

```
class turtle.Shape(type_, data)
Parameters:	type_ – one of the strings “polygon”, “image”, “compound”

Shape.addcomponent(poly, fill, outline=None)
Parameters:	
poly – a polygon, i.e. a tuple of pairs of numbers
fill – a color the poly will be filled with
outline – a color for the poly’s outline (if given)
```

* 提供了储存图形的数据结构.

|type_|data|
|:-|:-|
|“polygon”|a polygon-tuple, i.e. a tuple of pairs of coordinates|
|“image”|an image (in this form only used internally!)|
|“compound”|None (a compound shape has to be constructed using the addcomponent() method)|

#### 向量:Vec2D

```
class turtle.Vec2D(x, y)

a + b vector addition
a - b vector subtraction
a * b inner product
k * a and a * k multiplication with scalar
abs(a) absolute value of a
a.rotate(angle) rotation
```

* 提供了一些二维向量运算.

### 转换语言:write_docstringdict

```
turtle.write_docstringdict(filename="turtle_docstringdict")
Parameters:	filename – a string, used as filename
Create and write docstring-dictionary to a Python script with the given filename. This function has to be called explicitly (it is not used by the turtle graphics classes). The docstring dictionary will be written to the Python script filename.py. It is intended to serve as a template for translation of the docstrings into different languages.
```

### turtle配置文件

* 可以建一个turtle.cfg,每次import的时候会自动导入.
* cfg样式:

```
width = 0.5
height = 0.75
leftright = None
topbottom = None
canvwidth = 400
canvheight = 300
mode = standard
colormode = 1.0
delay = 10
undobuffersize = 1000
shape = classic
pencolor = black
fillcolor = black
resizemode = noresize
visible = True
language = english
exampleturtle = turtle
examplescreen = screen
title = Python Turtle Graphics
using_IDLE = False
```

* 前四行用于Screen.setup() 
* 5/6行用于Screen.screensize()
* shape 可以是任意内建图形.
* fillcolor 用于填充颜色.
* Lib/turtledemo目录下有一个turtle.cfg可以用来参考学习.

### 漂亮的turtledemo

* 用`python -m turtledemo`可以开启演示demo的总控台.
* 用`python -m turtledemo.demo名称`可以直接打开对应的演示demo


|Name|Description|Features|
|:-|:-|:-|
|bytedesign|complex classical turtle graphics pattern|tracer(), delay, update()|
|chaos|graphs Verhulst dynamics, shows that computer’s computations can generate results sometimes against the common sense expectations|world coordinates|
|clock|analog clock showing time of your computer|turtles as clock’s hands, ontimer|
|colormixer|experiment with r, g, b|ondrag()|
|forest|3 breadth-first trees|randomization|
|fractalcurves|Hilbert & Koch curves|recursion|
|lindenmayer|ethnomathematics (indian kolams)|L-System|
|minimal_hanoi|Towers of Hanoi|Rectangular Turtles as Hanoi discs (shape, shapesize)|
|nim|play the classical nim game with three heaps of sticks against the computer.|turtles as nimsticks, event driven (mouse, keyboard)|
|paint|super minimalistic drawing program|onclick()|
|peace|elementary|turtle: appearance and animation|
|penrose|aperiodic tiling with kites and darts|stamp()|
|planet_and_moon|simulation of gravitational system|compound shapes, Vec2D|
|round_dance|dancing turtles rotating pairwise in opposite direction|compound shapes, clone shapesize, tilt, get_shapepoly, update|
|sorting_animate|visual demonstration of different sorting methods|simple alignment, randomization|
|tree|a (graphical) breadth first tree (using generators)|clone()|
|two_canvases|simple design|turtles on two canvases|
|wikipedia|a pattern from the wikipedia article on turtle graphics|clone(), undo()|
|yinyang|another elementary example|circle()|