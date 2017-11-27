pylimit2
========

**作为pylimit的升级版，支持py3.6+，提供更合理方便的接口**

## 用法

先来一个觉得比较高级的，虽然还是没什么用，自定义检查

1. 自定义检查


    # 这里的Check是一个基类，check是装饰器
    from pylimit import Check, check
    
    # 首先定义自己的检查函数
    class MyCheck(Check):
        def check(self, parameter):
            # 为了简单，我直接就打印好了
            print("your input parameter is {}".format(parameter))
    
    @check(check_func=MyCheck)
    def test(a)
        print(a + 1)
    
    test()

2. 类型限定


    from pylimit import type_limit
    
    ＠type_limit
    def test(a: int, b: str, c: list) -> dict:
        print(a)
        print(b)
        print(c)
        return {'key': 'this is a test'}

3. 列表限定


    from pylimit import list_limit, type_limit
    # 装饰器可以一起使用
    @list_limit(a=(int, 2), b=(str, 3), default=0)
    @type_limit
    def test(a: list, b: list):
        print(a)
        print(b)

    test([1], ['string'])

## 感谢

写这个东西得要感谢两个人:

- @CreatCodeBuild  :+1:
- @MashiMaroLjc  :+1:

在Ｂ站上看了好多《西游记后传》片段的之后，无意中看到我动态中出现了_哲的王(CreatCodeBuild)_同学做的[视频](https://www.bilibili.com/video/av16567518/)，`python`强类型的执念。

然后觉得标题很有意思，就点进去看了一下，讲的就是给python加上一些限定。
突然想起来以前自己写过一段代码就想限定输入，觉得可能还是有点用的。然后就萌生了写这么一个小东西的念头。
点开_哲的王_同学的`github`，发现没有这个项目，就发邮件征询了他的同意准备开始写这个东西。
但是我一搜看看`github`上有没有类似的，竟然有一个出发点很相似的，而且发现竟然还是我在某个群认识人写过。
然后ＱＱ上联系，本来已经｀fork｀准备修改，改着改着就发现需要把原来@MashiMaroLjc写的代码基本全部删掉，那这样fork就没有意思了。
然后就自己开了一个｀pylimit2｀。


- 非常推荐看一下那个[视频](https://www.bilibili.com/video/av16567518/)
- 也非常推荐看一下另外一种思路，只利用装饰器，不涉及`__annotations__`的实现方式:https://github.com/MashiMaroLjc/pylimit

## 后记

诶，其实这个东西反正也没啥用，平时自己用用。本来写程序写程序就渣，当练练手
