#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 21:03:44
# @Author  : wentao (wentao@mgtv.com)
 
import os
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('..')
print sys.path
import tornado.ioloop
import tornado.web
from absc.controller.cms_controller import *
from absc.util.exception import *
from absc.handler.mainhandler import MainHandler

application = tornado.web.Application([
    (r"/cms/(.*)", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()