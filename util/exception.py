#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 22:58:31
# @Author  : wentao (wentao@mgtv.com)
 
import os
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')

from err import errcode

'''
exception.py文件，用作自定义异常
'''

class ApiException(Exception):

    def __init__(self, code, msg = None):
        self.err_code = code
        self.err_msg = msg if msg else errcode[code]