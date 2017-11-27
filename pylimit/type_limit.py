#!/usr/bin/env python
# created by Bruce Yuan on 17-11-26

from inspect import signature
import functools


def type_limit(func):
    """
    这是一个装饰器，用来限制函数的输入类型和返回类型
    :param func: 装饰器要装饰的函数,其中这个func每一个参数都需要确定类型
    :return: 
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = signature(func)
        bound_arguments = sig.bind(*args, **kwargs)

        # 检查输入参数的类型
        # 其实有这个for循环（本质上应该是getitem？），长度问题也会自动解决，只是我不知道该怎么提示好
        for name, value in bound_arguments.arguments.items():
            assert func.__annotations__[name] == type(value), \
                "param {} has to be type {}, but get type {}".format(
                    name,
                    func.__annotations__[name],
                    type(value)
                )
        if func.__annotations__.get('return', None):
            result = func(*args, **kwargs)
            # print(func.__name__)
            # 检查放回类型
            assert func.__annotations__['return'] == type(result), \
                "return type has to be type {}, but get type {}".format(
                    func.__annotations__['return'],
                    type(result)
                )
            return result
        else:
            return func(*args, **kwargs)
    return wrapper


def main():
    @type_limit
    def test(a: list, b: int, *, c: int) -> int:
        return a[0] + b + c

    result = test([1], b=2, c=5)
    print(result)


if __name__ == "__main__":
    main()
