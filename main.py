#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'aaugustyniak'

import Module

print "coding test ąśżź"
Module.function_in_module()
Module.dump_attributes()
Module.dump_caller_location()

for d in dir(Module):
    print "########################### module attr"
    print d
    print "########################### trying to call"
    f = getattr(Module, d)
    if callable(f):
        f()
    else:
        print f


print __author__