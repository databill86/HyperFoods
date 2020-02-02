#!/usr/bin/env python
# encoding: utf-8

class Option(object):
    _nil = object()
    def __init__(self, name, group, value=None):
        self.name = name
        self.value = value
        self.group = group
        self.__default = None
        self.__help = None
        self.__help = None

    def __call__(self, new_val=_nil):
        if new_val is not self._nil:
            print ("write to config")

        return self.type(self.value)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def help(self):
        return self.__help

    @help.setter
    def help(self, value):
        self.__help = value

    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, value):
        self.__default = value

    def set_value(self, value):
        self.value = value

    def _token(self):
        return '--{0.group.__name__}-{0.name}'.format(self)

    def __hash__(self):
        return hash(self._token())

    def __str__(self):
        ret = self._token()
        if self.value is not None:
            ret += '="{0.value}"'.format(self)
        return ret

    def __repr__(self):
        ret = '<Option {0.group.__name__}-{0.name}'.format(self, )
        if self.value is not None:
            ret += '={1.__name__}({0.value})'.format(self, type(self.value))
        if self.__default:
            ret += ' [default: %s]' % self.__default
        ret += '>'
        return ret
