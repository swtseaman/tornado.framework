#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-04 20:47:27
# @Author  : wentao (wentao@mgtv.com)
 
import os
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append('../..')
print sys.path
from absc.handler.handler import Handler
from absc.controller.cms_controller import *

class MainHandler(Handler):
    controller = {
        'test':CmsController
    }

    def get(self, action):
        #self.randerTemplate('', title = '标题')
        self.init()
        action = self.controller[action](self.params)
        action.getRun()
        contentType, content = action.getResult()
        self.writeResult(contentType, content)
        
    def post(self, action):
        self.init()
        action = self.controller[action](self.params)
        action.postRun()
        contentType, content = action.getResult()
        self.writeResult(a, b)