# -*- coding:utf-8 -*-
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
POST = '3306'
DATABASE = 'zlktqa_demo'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD,
                                                              HOSTNAME, POST, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
