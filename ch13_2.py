class Suji:
	def __init__(self,start):
		self.data=start
	def __sub__(self,other):
		return(self.data-other)
	def __add__(self,other)
		return(self.data+other)


class Bool:
	def __init__(self,start):
		self.data=start
	def __or__(self,other):
		return (self.data | other)

class Name:
	def __init__(self,start):
		self.data=start
	def __getslice__(self,low,high):
		return (self.data[low:high])


a=Name('abcde')

print (a.data[1:3])

