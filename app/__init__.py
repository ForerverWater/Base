# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 09:35:01
# @Author  : 赵国富 (175298292@qq.com)

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	CsrfProtect(app)

	db.init_app(app)
	login_manager.init_app(app)

	return app