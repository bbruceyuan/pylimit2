#!/usr/bin/env python
# created by Bruce Yuan on 17-11-26

from inspect import signature
from pylimit.limit_error import LimitError
from pylimit.type_limit import type_limit
import functools


def value_range(**info):
    """
    这个装饰器可以和type_limit一起使用
    其实最好是但你想设置连续值的时候可以使用　tuple 代替原来的　list
    :param info: 
    :return: 
    """
    # 假定默认是设置离散值
    continuous = info.get("continuous", False)
    val_range = info.get("value")

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            sig = signature(func)
            bound_arguments = sig.bind(*args, **kwargs)

            # 假如要设定连续值
            if continuous:
                for _, value in bound_arguments.arguments.items():
                    if not (val_range[0] < value < val_range[1]):
                        raise LimitError(
                            "the value range is from {name1} to {name2}".format(
                                name1=val_range[0],
                                name2=val_range[1]
                            )
                        )
            else:
                # 假如要设定离散值
                for _, value in bound_arguments.arguments.items():
                    if not (value in val_range):
                        raise LimitError(
                            "the value must in {name1}".format(
                                name1=val_range
                            )
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator


def main():
    """
    注释掉某些部分自己调试
    :return: 
    """
    @value_range(value=[1, 3])
    def test1(a, b):
        print(a + b)
    test1(1, 3)

    # 更吊一点的情况
    @value_range(value=[1, 3])
    @type_limit
    def test2(a: int, b: int) -> int:
        return a + b

    result2 = test2(1, 1)
    print(result2)

    # 更吊一点的情况
    @value_range(value=["1", "3"])
    @type_limit
    def test2(a: int, b: int) -> int:
        return a + b

    # value range 出错
    result2 = test2(1, 1)
    # type　出错
    re_ = test2('1', '3')
    print(re_)
    print(result2)


if __name__ == '__main__':
    main()
