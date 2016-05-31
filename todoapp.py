#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from flask import Flask
 
app = Flask(__name__)
 
from views import *
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nedev:torreon2014@localhost/todoapp' 
if __name__ == '__main__':
    app.run()
