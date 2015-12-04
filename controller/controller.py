#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 21:04:33
# @Author  : wentao (wentao@mgtv.com)
 
import os
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')
 
class Controller(object):

    def init(self, params):
        self.params = params
        self.contentType = {
            'xml':'text/xml',
            'js':'text/javascript',
            'css':'text/css',
            'json':'text/json',
            'html':'text/html'
        }

    def getRun(self):
        pass

    def postRun(self):
        pass

    def getResult(self):
        pass
