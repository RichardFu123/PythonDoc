# Python的max以及min
> python3.7
> 文档：
> https://docs.python.org/3/library/functions.html#max
> https://docs.python.org/3/library/functions.html#min
> https://blog.csdn.net/weixin_41084236/article/details/81875451

* 估计从最开始学python开始,没人没接触过max以及min这两个python的内建函数.
* 但这两个朴素的函数,其实也有一个相当好用的方法.
* sorted()方法里可以定义[key](https://blog.csdn.net/weixin_41084236/article/details/81875451)来实现自定义规则的排序.
* 而max和min里,也一样可以通过定义key来获取自定义规则的最值.

```
a = [2,2,2,2,3,1,"apple"]
print(max(a,key = a.count))
print(max(a,key = lambda x: x == "apple"))

print(min(a,key = a.count))
print(min(a,key = lambda x: x == "apple"))

 
====================== RESTART: F:\PyWorkspace\demo.py ======================
2
apple
3
2
>>> 
```

* 在效果上,min与max的key与sorted的key相似,具体可以在上面链接的文章里查看.