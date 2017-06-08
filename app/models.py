# -*- coding: utf-8 -*-
# @Date    : 2017-06-08 13:44:04
# @Author  : 赵国富 (175298292@qq.com)

import os
import hashlib
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db,login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True)
    username = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,**kwargs):
        super(User,self).__init__(**kwargs)

    @staticmethod
    def insert_user(email,username,password):
        user = User(email = email,username = username,password = password)
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('密码是不能读取的属性')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)