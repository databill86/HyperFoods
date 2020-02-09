#!/usr/bin/env python
# encoding: utf-8
from .base import DynamicModule
from .option import Option
import os


class OptionGroup(DynamicModule):
    _FactoryClass = Option

    def __getattr__(self, item):
        if item.startswith('__') and item.endswith('__'):
            if item is '__path__':
                return os.path.dirname(os.path.abspath(__file__))
            else:
                return

        if item not in self.instance:
            self.instance[item] = self._FactoryClass(item, self)
        return self.instance[item]


    def __setattr__(self, key, value):
        if key not in self.instance:
            self.instance[key] = self._FactoryClass(key, self, value)

        self.instance[key].set_value(value)


class OptionsModule(DynamicModule):
    _FactoryClass = OptionGroup

    def __iter__(self):
        out = self._defaultdict(list)
        for group in self.instance.values():
            for option in group.instance.values():
                out[group].append(option)

        return ((group, options) for group, options in out.items())
