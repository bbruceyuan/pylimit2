pylimit2
========

**作为[pylimit](https://github.com/MashiMaroLjc/pylimit)的升级版，给python的动态特性加上一些小小的约束，支持py3.5+，提供更合理方便的接口**

## 简介

就是可以像C++/Java一样在函数申明的时候加上一些类型约束，其实利用这个特性，你甚至像C++/Java一样申明数组（只要通过这个pylimit申明一个函数）

## 安装

如果你是想使用的话：
```
$ pip install pylimit2
```

其实还可以这样(最新版)：
```
$ pip install git+https://github.com/hey-bruce/pylimit2.git
```

当然这样也是没有问题的：
```
$ git clone https://github.com/hey-bruce/pylimit2.git
$ cd pylimit2
$ python setup.py install
```

## 用法

先来一个觉得比较高级的，虽然还是没什么用，自定义检查

1. 自定义检查

```
    # 这里的Check是一个基类，check是装饰器
    from pylimit import Check, check
    
    # 首先定义自己的检查函数
    class MyCheck(Check):
        def check(self, parameter):
            # 为了简单，我直接就打印好了
            # 这里的 parameter 的值就是我们函数调用时候的值，比如 test(1, [1, 2])
            # parameter 依次是 1, [1, 2]
            print("your input parameter is {}".format(parameter))
    
    # 这里 b 的值也可以是 OtherCheck
    @check(a=MyCheck， b=MyCheck)
    def test(a, b)
        print(a + b)
    
    test(1, 3)
```

2. 类型限定

```
    from pylimit import type_limit
    
    ＠type_limit
    def test(a: int, b: str, c: list) -> dict:
        print(a)
        print(b)
        print(c)
        return {'key': 'this is a test'}
    
    test(1, 'string', [1, 2, 3])
```

3. 列表限定

这个的用法比较多，后面再详细写

```
    from pylimit import list_limit, type_limit
    
    # 装饰器当然可以一起使用
    @list_limit(a=(int, 2), b=(str, 3), default=0)
    @type_limit
    def test(a: list, b: list):
        print(a)
        print(b)

    test([1], ['string'])
```

4. 元组限定

和列表基本是一样的

```
    @tuple_limit(a=[int, str, dict])
    @type_limit
    def test(a: tuple):
        print(a)

    test((1, "string", {}))
```

5. 参数范围

范围是离散值(默认) => 推荐使用列表设定范围

```
    from pylimit import value_range
    
    @value_range(value=[1, 3])
    def test1(a, b):
        print(a + b)
    test1(1, 3)
```

范围是连续的 => 推荐使用元组设定范围

```
    from pylimit import value_range
    
    @value_range(value=(1, 3), continuous=True)
    def test1(a, b):
        print(a + b)
    test1(1, 3)
```

6. const变量

一种使用 类 Const, 只能用  obj.value 获得值，不能设定

```
    a = Const(1)
    print(a.value)
```

另外一种利用字典来做

```
    my_const = ConstValue()
    my_const.HELLO_WORLD = "hello world"
    print(my_const.HELLO_WORLD)
```

后面如果有时间或者有人真的觉得有点用，或者哪怕只是有一些像我一样的新手想学习一下，我可能就把文档写的详细一点了

> 其实在代码里面都写了一些测试用例，都放在每个函数的main()里面了

## 感谢

写这个东西得要鸣谢两个人:

- @[CreatCodeBuild](https://github.com/CreatCodeBuild)  :+1:
- @[MashiMaroLjc](https://github.com/MashiMaroLjc)  :+1:

推荐`follow`楼上两位大佬

## 后记

其实我是在Ｂ站上看完好多《西游记后传》片段的之后，脑子里面全是鬼畜:joy:2333，然后无意中看到我动态中出现了_哲的王(CreatCodeBuild)_同学做的[视频](https://www.bilibili.com/video/av16567518/)，`python`强类型的执念。觉得很有意思，就点进去看了一下，讲的就是给python加上一些限定。突然想起来以前自己写过一段代码就想限定输入，觉得可能还是有点用的。然后就萌生了写这么一个小东西的念头。点开_哲的王_同学的`github`，发现没有这个项目，就发邮件征询了他的同意准备开始写这个东西。但是我一搜看看`github`上有没有类似的，竟然有一个出发点很相似的，而且发现竟然还是我在某个群认识人写过。然后ＱＱ上联系，本来已经`fork1`准备修改，改着改着就发现需要把原来@MashiMaroLjc写的代码基本全部删掉，那这样fork就没有意思了。然后就自己开了一个`pylimit2`。

- 非常推荐看一下那个[视频](https://www.bilibili.com/video/av16567518/)
- 也非常推荐看一下[MashiMaroLjc](https://github.com/MashiMaroLjc)提供的另外一种思路，只利用装饰器，不涉及`__annotations__`的实现方式:https://github.com/MashiMaroLjc/pylimit

其实这两个方式也都差不多，而且这个东西就像楼上两位说的一样反正也没啥用，平时自己用用。本来写程序写程序就渣，当练练手
