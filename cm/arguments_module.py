#!/usr/bin/env python
# encoding: utf-8
from .base import DynamicModule
from .arguments import Argument


class ArgumentsModule(DynamicModule):
    _FactoryClass = Argument
