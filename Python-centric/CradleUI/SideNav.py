from CoreUI import UIElement

class NavElem():
	def __init__(self,title,children):
		self.title = title
		self.children = children

class SideNav(UIElement):
	def __init__(self):
		self.registerCSS('''<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">''')
		self.elements = []
	def buildFromFileTree(self,ft):
		pass
	def addElem(self,e):
		self.elements.append(e)
	def render(self):
		

