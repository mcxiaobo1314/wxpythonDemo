#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
	设置背景图控制器
'''
class BackgroundController:
	def __init__(self,Main,Wx):
		self.Main = Main
		self.Wx   = Wx
		#self.w,self.h = self.Main.frame.GetSize()
		#self.Main.Bind(self.Wx.EVT_SIZE, self.change)
		self.setBackground()

	def setBackground(self):
		#sizer = self.Wx.GridBagSizer(0, 0)
		#设置背景图并绑定方法
		bg = self.Wx.Image("static/img/222.jpg",self.Wx.BITMAP_TYPE_ANY)
		bg = bg.Mirror(horizontally = True)
		w,h = self.Main.frame.GetSize()
		bg.Rescale(w,h)
		pic = bg.ConvertToBitmap()
		bg = self.Wx.StaticBitmap(self.Main.frame.panel,-1,pic,(0,0))
		#sizer.Add(bg,pos=(0,0),span=(0,0),flag=self.Wx.EXPAND|self.Wx.ALL,border=5)
		#self.Main.frame.panel.SetSizerAndFit(sizer)
		#print self.Wx.DisplaySize()

	def change(self,event):
		pass
