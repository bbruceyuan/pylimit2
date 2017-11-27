#!/usr/bin/env python
# created by Bruce Yuan on 17-11-26

# 哇，今天这也太蠢了，我竟然想着实现一个const list....　tuple　已经设计的这么完美了
# 脑子一抽，又想实现一个const dict。如果　dict　要是静态的了真的一点用处都没有
# 最后思考了好久好久，只能提供另外一种思路，直接放到字典里面，然后检查那个东西有没有使用过

from pylimit.limit_error import LimitError
from pylimit.const_error import ConstError


class Const:
    """
    attention: the code were writen by fat_rabbit. but I change the last line, replace LimitError　with ConstError
    link: https://github.com/MashiMaroLjc/pylimit/blob/master/pylimit.py
    
    The class of const.But only can build it for int ,float or str

    """
    def __init__(self, value):
        if not isinstance(value, (int, str, float)):
            raise LimitError("You only can set the value of int ,float or str!")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        raise ConstError("You can't change the value!")


# 下面提供另外一种思路去实现一个 const 的类
class ConstValue:
    """
    实现const类的第二种方法
    
    假如你需要在你项目里面用到比较多的const的话，其实比较建议这种方式
    
    这里主要事想利用dict的特性
    """
    def __setattr__(self, key, value):
        print(key)
        if self.__dict__.get(key, None):
            raise ConstError("you are trying to change the  const.{}".format(key))
        else:
            self.__dict__[key] = value

    def __getattr__(self, key):
        if self.__dict__.get(key, None):
            return self.key
        else:
            raise Exception('there is no const named {}'.format(key))


def main():
    # type one
    a = Const(1)
    print(a.value)

    # type two
    my_const = ConstValue()
    my_const.HELLO_WORLD = "hello world"
    print(my_const.HELLO_WORLD)


if __name__ == '__main__':
    main()
