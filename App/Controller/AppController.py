#!/usr/bin/python
# -*- coding: UTF-8 -*-

import App.Controller.BackgroundController as Background
import App.Controller.ButtonController as Button
import App.Controller.InputController as Input
import App.Controller.MenuController as Menu

'''
	公共控制器加载类
'''
class AppController:
	
	'''
	   构造函数方法
	   @param Object  Main   是Main 类
	   @param Object  Wx     wx框架类
	'''
	def __init__(self,Main,Wx):
		self.Main = Main
		self.Wx  = Wx
		self.moduleInit()


	'''
	  模块初始化
	'''
	def moduleInit(self):
		Background.BackgroundController(self.Main,self.Wx)
		Menu.MenuController(self.Main,self.Wx)
		Button.ButtonController(self.Main,self.Wx)
		Input.InputController(self.Main,self.Wx)
