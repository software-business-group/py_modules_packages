#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'aaugustyniak'

import Package

Package.submod_a()
Package.SubModB.submod_b()

from Package import *

submod_a()
SubModB.submod_b()
