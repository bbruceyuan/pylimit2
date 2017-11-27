#!/usr/bin/env python
# created by Bruce Yuan on 17-11-27


class ConstError(Exception):
    def __init__(self, message):
        self._message = str(message)

    def __str__(self):
        return self._message

    __repr__ = __str__
