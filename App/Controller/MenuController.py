#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
	菜单控制器
'''
class MenuController:
	'''
	   构造函数方法
	   @param Object  Main   是Main 类
	   @param Object  Wx     wx框架类
	'''
	def __init__(self,Main,Wx):
		self.Main = Main
		self.Wx  = Wx
		self.menuBar = self.Wx.MenuBar()
		self.menu = self.Wx.Menu()
		self.setMenu()
		self.Main.frame.SetMenuBar(self.menuBar)	


	def setMenu(self):
		jieShao = self.menu.Append(self.Wx.NewId(),"&介绍")
		self.Main.Bind(self.Wx.EVT_MENU,self.about,jieShao)
		self.menuBar.Append(self.menu,"&目录")


	def about(self,event):
		dialog = self.Wx.Dialog(self.Main.frame.panel,-1,"demo介绍",size=(200,200))
		panel = self.Wx.Panel(dialog)
		name = self.Wx.StaticText(panel,label="姓名:demo",pos=(0,0))
		name.SetForegroundColour('red')
		self.Wx.StaticText(panel,label="出生年:2000年",pos=(0,20))
		self.Wx.StaticText(panel,label="惯籍:未知",pos=(0,40))
		self.Wx.StaticText(panel,label="国籍:中国",pos=(0,60))
		rect = dialog.ShowModal()
		


