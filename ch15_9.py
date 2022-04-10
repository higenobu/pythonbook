class Windex:
	def __getitem__(self,suji):
		return suji*3
a=Windex()
for ii in range(10):
	print (a[ii])


class Wsample:
	def __getitem__(self,ii):
		return self.data[ii]

b=Wsample()
b.data="abcd"
for ww in b:
		print (ww)

