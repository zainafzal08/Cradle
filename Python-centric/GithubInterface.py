from github import Github
import getpass

class FileTree():
	def __init__(self,name,root):
		self.name = name
		self.root = root
		self.children = {}
	def addNodeFromPath(self,path):
		pathList = path.split("/")
		if path[0:len(self.root)] != self.root:
			return
		currLevel = self.children
		while len(pathList) > 0:
			head = pathList[0]
			if head in currLevel:
				currLevel = currLevel[head]
			else:
				currLevel[head] = {}
				currLevel = currLevel[head]
			pathList = pathList[1:]
	def show(self,**kargs):
		nodes = self.children
		indent = 0
		if "nodes" in kargs:
			nodes = kargs["nodes"]
		if "indent" in kargs:
			indent = kargs["indent"]
		for k in nodes.keys():
			print("  "*indent + k)
			self.show(nodes=nodes[k],indent=indent+1)

class Connection():
	def __init__(self,username,password):
		self.auth = {"user":username,"pass":password}
	def getFileStructure(self,repoName,root):
		g = Github(self.auth["user"], self.auth["pass"])
		repo = g.get_user().get_repo(repoName)
		sha = repo.get_branch("master").commit.sha
		tree = FileTree(repoName+" File Tree",root)
		raw = repo.get_git_tree(sha,recursive=True).tree
		for elem in raw:
			tree.addNodeFromPath(elem.path)
		tree.show()

if __name__ == "__main__":
	# testing
	user = raw_input("Username: ")
	password = getpass.getpass()
	con = Connection(user,password)
	con.getFileStructure("Notes","COMP3131-Notes")
