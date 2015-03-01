import os

class Manager(object):
	def __init__(self, path):
		# declare fields
		self.fileList = []
		
		# create list of managed files
		if os.path.isdir(path):
			index = 1
			for root, dirnames, filenames in os.walk(path):
				for filename in filenames:
					self.fileList.append([filename, root])
		else:
			raise Exception(path + " is invalid")
	
	def getContents(self):
		return self.fileList
