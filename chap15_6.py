#ch15-6
class Human:
	def setname(self,name):
		self.name=name
	def display(self):
		print (self.name)

a=Human()
b=Human()


a.setname("山田太郎")
b.setname("大阪次郎")
a.display()
b.display()

class Student(Human):
	def school(self,schoolname):
		self.schoolname=schoolname
	def display(self):
		print (self.name,self.schoolname)
s=Student()
s.setname("Masa Matsuo")
s.school("UCLA")
s.display()

class Child(Student):
	def __init__(self,name):
		self.name=name
	def __eq__(self,other):
		 if(self.schoolname==other.schoolname): return True
		 else: return False 
		 
	
c=Child('akira')
c.school("UCSB")
c.display()
d=Child('yamada')
d.school("UCSB")
e=c==d
print (e)


class Newclass:
	def display(self,text):
		print (text)

aa=Newclass()
aa.display('python textbook')

Newclass.display(aa,'Python Textbook')


class Supclass1:
	def setname(self,name):
		self.name=name
	def method(self):
		print ('ABC')


a=Supclass1()
a.method()


class Subclass1(Supclass1):
	print ('subclass1 begins')
	def display(self):
		print (self.name)	
	print ('subclass1 end')

b=Subclass1()
b.setname('PHP')
b.display()

