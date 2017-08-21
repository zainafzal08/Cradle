class UIElement():
	def render(self):
		return "<h1 style='color: red;'>UI ELEMENT NOT IMPLEMENTED</h1>"
	def registerCSS(self,line):
		if not hasattr(self,"dependencies"):
			self.dependencies = []
		self.dependencies.append(line)

def 