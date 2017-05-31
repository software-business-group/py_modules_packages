#!/usr/bin/python
# -*- coding: utf-8 -*-

'''order matters'''
import sys
sys.path.append('./some_folder')
import OtherModule
others_list = ['../.idea', '../shebang_coding']
sys.path.extend(others_list)


import OtherPackage as Package

Package.submod_a()
Package.SubModB.submod_b()

from Package import *

submod_a()
SubModB.submod_b()




print sys.path
print "############# MODULY #################"
print sys.modules
print "############# Klucze #################"
print sys.modules.keys()



