from CradleUI.SideNav import SideNav
from CradleUI.SideNav import NavElem

class CradleModule():
	def __init__(self,name,renderable):
		self.name = name
		self.renderable = renderable

class Cradle():
	def __init__(self):
		self.elements = []
		self.initSideNav()
	def initSideNav(self):
		labs = NavElem("Labs",[])
		labs.children.append(NavElem("Lab 1",[]))
		labs.children.append(NavElem("Lab 2",[]))
		lectures = NavElem("Lectures",[])
		lectures.children.append(NavElem("Lecture 1",[]))
		lectures.children.append(NavElem("Lecture 2",[]))
		nav = SideNav()
		nav.addElem(labs)
		nav.addElem(lectures)
		self.elements.append(CradleModule("sideNav",nav))
	def getkargs(self):
		d = {}
		for e in self.elements:
			d[e.name] = e.renderable.render()
		return d