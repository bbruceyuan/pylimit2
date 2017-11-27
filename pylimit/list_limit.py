#!/usr/bin/env python
# created by Bruce Yuan on 17-11-26
from inspect import signature
from pylimit.limit_error import LimitError
import functools


def check_type(value, type1):
    """
    判断两个类型是否一致
    :param value: 
    :param type1: 
    :return: bool
    """
    if not isinstance(value, type1):
        raise LimitError(
            "you set {} type, but get a {} in parameters".format(
                type1,
                type(value)
            )
        )
    return True


def _check(values, type1):
    """
    检查某个数组里面的东西是否全部是某个类型
    :param values: list
    :param type1 one type
    :return: 
    """
    for value in values:
        check_type(value, type1)
    return True


def fill_list(list_, set_length, default):
    """
    对列表进行填充，如果length长度超过了list_的长度，报错
    :param list_: 原始列表
    :param set_length: 扩充的长度
    :param default: 默认填充项
    :return: None
    """
    length = set_length - len(list_)
    if length == 0:
        pass
    elif length > 0:
        list_.extend([default for _ in range(length)])
    else:
        raise LimitError(
            "you set the list length is {}, but get the length {}".format(
                set_length,
                len(list_)
            )
        )


def list_limit(*param, **info):
    """
    对列表进行限制
    :param param: 
    :param info: 
    :return: 
    
    usage:
    ＠list_limit(parm=(3, 4, 5), type=int)
    ＠type_limit
    创建三个长度分别为３，４，５的类型为int的列表
    
    ＠list_limit(a=(int, 3), b=(str, 4), default=None)
    @type_limit
    创建长度为３的int列表，长度为4的str列表，如果函数输入值要小于默认的长度，填入None
    
    @list_limit(a=[int, str, int], b=[str, dict])
    @type_limit
    创建的列表长度分别为３，２，列表里面的元素类型如上面列表所示
    
    @list_limit(a=(int, 3), b=[int, str, dict])
    @type_limit
    你甚至可以像上面一样混用这两种方式
    """
    input_type = info.get('type', None)
    default = info.get('default', None)

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = signature(func)
            bound_arguments = sig.bind(*args, **kwargs)
            # 加入按照第一种方式输入
            if input_type is not None:
                # 判断每一个列表
                # 在这里要的只是每一个参数项的值，不需要它的名字
                for i, value in enumerate(bound_arguments.arguments.values()):

                    # 检查每个输入列表中的每一项是否都为input_type
                    _check(value, input_type)

                    # 对列表进行填充
                    fill_list(value, param[i], default)

            # 加入想按照第一种方式设置却没有设置默认的类型
            elif len(param) > 0:
                raise LimitError(
                    "you did not set the list type"
                )
            else:
                for name, value in bound_arguments.arguments.items():
                    # 这里需要分成两种情况
                    # 一种是给每个列表设置同一种类型，输入参数就是一个 tuple
                    # 另一种是给列表里面的每个元素设置不同的类型,输入参数为一个 list
                    if isinstance(info.get(name), tuple):

                        # 检查第一项是否是　list
                        # print(info.get(name)[0])

                        if info.get(name)[0] == list:
                            # ie. info.get(name) => (list, [(int, 3), (int, 3)])
                            sub_list = info.get(name)[1]
                            if isinstance(sub_list, list):
                                # 先检查输入参数里面的东西是不是列表
                                _check(value, list)
                                # 使用列表填充
                                fill_list(value, len(sub_list), [])

                                for index, each_tuple in enumerate(sub_list):
                                    _check(value[index], each_tuple[0])
                                    fill_list(value[index], each_tuple[1], default)
                                    # check()
                                    pass
                                # print(value)
                                # print(sub_list)
                            else:
                                raise LimitError(
                                    "set a 2D array, the second param should be a tuple"
                                )
                        # 如果第一项不是list，而是str, int, float之类的，
                        # 其实是其他的也可以，只是后面可能会报错
                        else:
                            # 首先要检查输入列表中每一项是否为input_type
                            # info.get(name) => （int, 4)
                            _check(value, info.get(name)[0])
                            # 填充列表
                            fill_list(value, info.get(name)[1], default)

                    # 另一种是给列表里面的每个元素设置不同的类型,输入参数为一个 list
                    elif isinstance(info.get(name), list):
                        # 一开始这个check函数不该那样写的，所以现在在这里失效了，难受
                        # 判断输入参数，即列表中每一个参数都和设定类型相对应
                        length = len(value)
                        type_list = info.get(name)
                        if length == len(type_list):

                            for _ in range(length):
                                check_type(value[_], type_list[_])
                        # 输入列表参数长度和设定的长度不等
                        else:
                            raise LimitError(
                                "you set the length is {}, but the get length is {}".format(
                                    info.get(name).__len__(),
                                    length
                                )
                            )
                        pass
                pass
            return func(*args, **kwargs)
        return wrapper
    return decorator


def main():
    @list_limit(1, 2, 3, type=int, default=0)
    def test1(a, b, c):
        print(a)
        print(b)
        print(c)

    test1([2], [2], [4])

    @list_limit(a=(int, 3), b=(int, 3), default=None)
    def test2(a, b):
        print(a)
        print(b)

    # test2([1, 3], [1])

    @list_limit(a=[int, str, int])
    def test3(a):
        print(a)

    # test3([1, 'a', 4])

    @list_limit(a=(list, [(int, 3)]), b=(list, [(int, 3), (str, 4)]))
    def test4(a, b):
        print(a)
        print(b)

    test4([[1, 3, 4]],
          [[5, 6, 7]])


if __name__ == '__main__':
    main()
