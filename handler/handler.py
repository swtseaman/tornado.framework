#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 21:03:44
# @Author  : wentao (wentao@mgtv.com)
 
import os
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web

'''
Handler基类，用于实现基本RequestHandler方法
'''
class Handler(tornado.web.RequestHandler):

    '''
    初始化
    init()
    接收所有参数，并保存为字典params
    '''
    def init(self):
        param = self.request.arguments
        _params = {}
        for key in param:
            _params[key] = self.get_argument(key)
        self.params = _params

    '''
    输出结果
    writeReuslt(contentType, content)
    contentType:设置输出结果类型，如：text/html, text/javascript
    content:输出内容主体
    '''
    def writeResult(self, contentType, content):
        self.set_header('Content-Type', contentType)
        self.write(content)

    '''
    渲染模版
    renderTemplate(templateName, **kwargs)
    templateName:模版路径
    **kwargs:模版参数（参数个数无限制），如：title = '标题', orderList = ol ...
    '''
    def randerTemplate(self, templateName, **kwargs):
        self.render(templateName, kwargs)