#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import importlib
import Config.Config as Config

class App:
	'''
	   构造函数方法
	   @param Object  Main   是Main 类
	   @param Object  Wx     wx框架类
	'''
	def __init__(self,Main,Wx):
		self.Main = Main
		self.Wx  = Wx

	'''
	  自动加载
	'''
	def autoload(self):	
		self.autoloadParams(Config.autoloadFile)

	'''
		自动加载模块
		@param  Array config  配置参数
	'''
	def autoloadParams(self,config):
		for name in config:
			module = importlib.import_module(name)
			arr = name.split('.')
			getattr(module,arr[-1])(self.Main,self.Wx)


