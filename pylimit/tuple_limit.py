#!/usr/bin/env python
# created by Bruce Yuan on 17-11-27
from inspect import signature
from pylimit.limit_error import LimitError
from pylimit.list_limit import check_type
from pylimit.type_limit import type_limit
import functools


def tuple_limit(**info):
    """
    这个其实和 list_limit基本是一样的，可是需要考虑到 tuple　基本是不会变化的
    而且tuple一般在传值的时候也都是固定的，所以不会扩展
    所以这里就只提供一种限定方式
    对传入的参数每一项进行对应。
    ie. 
    def test(a):
        print(a)
    
    我们希望 a 里面每一项分别对应，即假如我们希望这个 tuple的形式为 a = [str, int, dict]
    那么我们就加上装饰器
    @tuple_limit(a=[str, int, dict])
    def test(a):
        pass
    
    当然其实这个很好扩展，只是觉得用处不大，如果你想做成原来那种list_limit中 a = (int, 3) 
                                                ==> 表示这个tuple中有三个int型的数据
    如果你想使用别的限制，其实这个库提供了一种更好用的方式，那就是自定义限定，具体可以查看自定义check如何使用                                                        
    :param info: 
    :return: 
    """
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = signature(func)
            bound_arguments = sig.bind(*args, **kwargs)

            for name, value in bound_arguments.arguments.items():
                input_type = info.get(name)
                length = len(input_type)

                if len(value) == length:
                    # 检查每一项是否对应
                    for i in range(length):
                        check_type(value[i], input_type[i])
                else:
                    raise LimitError(
                        "the set type length is {}, but the input parameter length is {}".format(
                            length,
                            len(value)
                        )
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator


def main():

    @tuple_limit(a=[int, str, dict])
    @type_limit
    def test(a: tuple):
        print(a)

    test((1, "string", {}))


if __name__ == '__main__':
    main()
