#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import App.App as App

'''
  App框架类
'''
class Frame(wx.Frame):
	def __init__(self,parent,id=-1,title = "",pos = wx.DefaultPosition,size = (-1,-1),style = wx.DEFAULT_FRAME_STYLE,name = "demo"):
		super(Frame,self).__init__(parent,id,title,pos,size,style,name)
		self.panel = wx.Panel(self)
	
'''
	App应用入口
'''
class Main(wx.App):
	def OnInit(self):
		self.frame = Frame(None,title ="demo")
		self.SetTopWindow(self.frame)
		app = App.App(self,wx)
		app.autoload()
		self.frame.Show()
		return True

	def OnExit(self):
		print "xxxx"

'''
  初始化入口
'''
if __name__ ==  "__main__":
	#app = wx.PySimpleApp()
	app = Main(False)
	app.MainLoop()
