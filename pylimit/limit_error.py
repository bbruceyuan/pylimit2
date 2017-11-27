#!/usr/bin/env python
# created by Bruce Yuan on 17-11-26


class LimitError(Exception):
    """
    attention: the code were writen by fat_rabbit
    link: https://github.com/MashiMaroLjc/pylimit/blob/master/pylimit.py
    The Exception maybe will be raise during you use pylimit.
    """

    def __init__(self, message):
        self._message = str(message)

    def __str__(self):
        return self._message

    def __repr__(self):
        return self._message
