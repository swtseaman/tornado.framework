#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 21:33:36
# @Author  : wentao (wentao@mgtv.com)
 
import os
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')
#sys.path.append('..')
from controller import Controller

class CmsController(Controller):
    def __init__(self, params):
        self.init(params)

    def getRun(self):
        pass

    def postRun(self):
        pass

    def getResult(self):
        return self.contentType['json'], '{msg:%s}' % self.params['name']