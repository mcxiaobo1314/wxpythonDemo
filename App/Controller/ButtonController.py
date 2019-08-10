#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx.lib.buttons as buttons


'''
	按钮控制器
'''
class ButtonController:
	'''
	   构造函数方法
	   @param Object  Main   是Main 类
	   @param Object  Wx     wx框架类
	'''
	def __init__(self,Main,Wx):
		self.Main = Main
		self.Wx   = Wx
		self.setButton()

	def setButton(self):
		pass
		#self.Button = self.Wx.Button(self.Main.frame.panel,label='第一个程序',pos=(10,0))

		#设置按钮加载背景图
		#buttonBmp = self.Wx.Image("static/img/button.jpeg",self.Wx.BITMAP_TYPE_ANY)
		#w = buttonBmp.GetWidth() / 5
		#h = buttonBmp.GetHeight()/ 4 
		#buttonBmp.Rescale(w,h)
		#buttonBmp = buttonBmp.ConvertToBitmap()
		#self.Button = self.Wx.BitmapButton(self.Main.frame.panel,-1,buttonBmp,pos=(0,0))
		#self.Button.SetDefault()
		#self.Main.Bind(self.Wx.EVT_BUTTON,self.aubot,self.Button)


		#设置按钮
		#sizer = self.Wx.FlexGridSizer(1,3,20,20)
		#b = self.Wx.Button(self.Main.frame.panel,-1,"关于demo")
		#b.SetDefault()
		#sizer.Add(b)
		#self.Main.Bind(self.Wx.EVT_BUTTON,self.aubot,b)

	#def aubot(self,event):
	#	dlg = self.Wx.MessageDialog(None,u"功能开发中",u"关于demo的故事",self.Wx.YES_NO)
	#	if dlg.ShowModal() == self.Wx.ID_YES:
	#		dlg.Close(True)
	#	dlg.Destroy()


