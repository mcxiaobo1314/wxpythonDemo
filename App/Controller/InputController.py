#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
	输入框控制器
'''
class InputController:
	'''
	   构造函数方法
	   @param Object  Main   是Main 类
	   @param Object  Wx     wx框架类
	'''
	def __init__(self,Main,Wx):
		self.Main  = Main
		self.Wx   = Wx 
		self.setInput()

	def setInput(self):
		pass
		#设置输入框
		#hbox = self.Wx.BoxSizer(self.Wx.HORIZONTAL)
		#sizer = self.Wx.FlexGridSizer(50,50,30,-1)
		#title = self.Wx.StaticText(self.Main.frame.panel,label="请输入名字")
		#tc = self.Wx.TextCtrl(self.Main.frame.panel)
		#sizer.AddMany(
		#	[(title,0,self.Wx.ALIGN_RIGHT),(tc,0,self.Wx.SHAPED)]
		#)
		#sizer.AddGrowableCol(1,1)
		#hbox.Add(sizer,proportion=1,flag=self.Wx.ALL|self.Wx.EXPAND,border=15)
		#self.Main.frame.panel.SetSizer(hbox)