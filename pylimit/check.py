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

            for value in bound_arguments.arguments.values():
                check_func = info.get('check_class')()
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

    @check(check_class=MyCheck)
    def test(a):
        print(a)

    test(1)


if __name__ == '__main__':
    main()
