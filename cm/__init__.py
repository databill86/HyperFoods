#!/usr/bin/env python
# encoding: utf-8
import sys
import re
from .options_module import OptionsModule
from .arguments_module import ArgumentsModule

class Importer(object):
    def find_module(self, fullname, path=None):
        if fullname.startswith('cm.'):
            return self

    def load_module(self, name):
        l = name.split('.')
        l.pop(0)
        if len(l) == 1:
            if l[0] == 'options':
                return sys.modules[__name__].options
            elif l[0] == 'arguments':
                return sys.modules[__name__].arguments
        if len(l) == 2:
            if l[0] == 'options':
                option = sys.modules[__name__].options.__getattr__(l[1])

                return option
            # elif l[0] == 'arguments':
                # return sys.modules[__name__].arguments.__getattr__(l[1])



def parse_command_line():
    argv = sys.argv[1:]
    _opts_expr = re.compile(r"^\-+(?P<group>\w+)\-(?P<key>\w+)([\=\s](?P<value>.*))?$")
    options = sys.modules[__name__].options

    for option in filter(lambda x: x.startswith('-'), argv):
        matcher = _opts_expr.match(option)
        if matcher is not None:
            opt = matcher.groupdict()
            value = opt['value']
            value = value if value is not None else value
            group = getattr(options, opt['group'])
            setattr(group, opt['key'], value)
        else:
            if option in ('--help', '-h'):
                print ("List of available program options:")
                for group, opts in options:
                    print('Group "%s"' % group.__name__)
                    for opt in group:
                        if opt.help is not None:
                            print ("\t%-15s\t%s%s" % (
                                opt,
                                opt.help,
                                ' [default: "%s"]' % opt.default if opt.default else '')
                            )
                        else:
                            print ("\t%s" % opt)
                    print("\n")
                exit(0)

            elif option in ('--config', '-c'):
                print 'Load config'


sys.modules[__name__].options = OptionsModule('options')
sys.modules[__name__].arguments = ArgumentsModule('arguments')

if sys.meta_path:
    sys.meta_path.insert(0, Importer())
else:
    sys.meta_path = [Importer()]


__all__ = ('options', 'arguments', 'parse_command_line')