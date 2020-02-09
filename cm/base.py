#!/usr/bin/env python
# encoding: utf-8
import types
from collections import defaultdict

class DynamicModule(types.ModuleType):
    _INSTANCES = defaultdict(dict)
    _FactoryClass = None
    _defaultdict = defaultdict

    @property
    def instance(self):
        return self._INSTANCES[self.__name__]

    def __getattr__(self, item):
        if item not in self.instance:
            self.instance[item] = self._FactoryClass(item)
        return self.instance[item]

    def __iter__(self):
        for key in self.instance.values():
            yield key
