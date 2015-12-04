#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 22:58:31
# @Author  : wentao (wentao@mgtv.com)
 
import os
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')

errcode = {}

errcode['001'] = '非法请求'
errcode['002'] = '缺少参数'