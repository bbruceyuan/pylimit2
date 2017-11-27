#!/usr/bin/env python
# created by Bruce Yuan on 17-11-27
import functools
from inspect import signature


class Check:
    """
    这就是让用户自定义check
    这样可以方便扩展，想怎么检查参数就怎么检查参数
    """

    def check(self, parameter):
        pass


def check(**info):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = signature(func)
            bound_arguments = sig.bind(*args, **kwargs)

            for name, value in bound_arguments.arguments.items():
                # 会优先使用check_class，所以check_class只需要一个
                # 这样就表示对所有的参数使用同一个函数去检查
                check_func = info.get('check_class', None) or info.get(name)()

                if isinstance(check_func, Check):
                    check_func.check(value)
                else:
                    raise Exception(
                        "your check class must inherit from the base Check class"
                    )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def main():

    # 自定义的check类必须Check基类继承下来
    class MyCheck(Check):
        def check(self, parameter):
            print("this is the {}".format(parameter))

    @check(a=MyCheck)
    def test(a):
        print(a)

    test(1)


if __name__ == '__main__':
    main()
