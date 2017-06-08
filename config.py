# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 09:24:47
# @Author  : 赵国富 (175298292@qq.com)

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_RECORD_QUERIES = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	                 'mysql://root:2wsx!QAZ@192.168.0.203:3306/wind?charset=utf8'
	SECRET_KEY = 'Base'
	WTF_CSRF_SECRET_KEY = 'random key for form'

	@staticmethod
	def init_all(app):
		pass
