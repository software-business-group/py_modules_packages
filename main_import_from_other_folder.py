#!/usr/bin/python
# -*- coding: utf-8 -*-

'''order matters'''
import sys
sys.path.append('./some_folder')
import OtherModule
others_list = ['../.idea', '../shebang_coding']
sys.path.extend(others_list)
import first

OtherModule.function_in_other_module()
print sys.path





