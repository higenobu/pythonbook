#!/usr/bin/env python
import sys
import csv
import pickle
class Employee(object):

	def __init__(self,ssn,fname,lname,bod,address,tel,sal,kubun):
		self.ssn=ssn
		self.fname=fname
		self.lname=lname
		self.bod=bod
		self.address=address
		self.tel=tel
		self.sal=0
		self.kubun=kubun
	


	def add_sal(self,up):
		self.sal=self.sal+up

	def  __repr__(self):

		return repr("ssn=%s,fname=%s,lname=%s,bod=%s,address=%s,tel=%s,sal=%s" % (self.ssn,self.fname,self.lname,self._bod,self._address,self._tel,self.sal))

#emp=Employee(ssn='999-999-1111',fname='akira',lname='matsuo',bod='2000-01-01',address='aaaaa',tel='999-999-9999')
#print (emp)
#print (emp.lname)
#print (emp)
#,ssn,lname,fname,bod,address,tel
class Staff(Employee):
	def __init__(self,ssn,fname,lname,bod,address,tel,sal,kubun):
		super().__init__(ssn,fname,lname,bod,address,tel,sal,kubun)
		
	def add_sal(self,up):
		self.sal=self.sal+up
			
	def  __repr__(self):

		return repr("ssn=%s,fname=%s,lname=%s,bod=%s,address=%s,tel=%s,kubun=%s,sal=%d" % (self.ssn,self.fname,self.lname,self.bod,self.address,self.tel,self.kubun,self.sal))



wst=Staff(ssn='999-999-1111',fname='akira',lname='matsuo',bod='2000-01-01',address='aaaaa',tel='999-999-9999',kubun='waiter',sal=100)

#print (wst)
#print (wst.kubun)
def load_emp(filename):
	global empnow
	with open(filename,'rb') as inf:
		empnow=pickle.load(inf)

#emp=Employee(ssn='999-999-1111',fname='akira',lname='matsuo',bod='2000-01-01',address='aaaaa',tel='999-999-9999',kubun='AA',sal=100)

emplist=[]


for ii in range(2):
	ssn=input("ssn")
	fname=input("fname")
	lname=input("lname")
	bod=input("bod:")
	address=input("address:")
	tel=input("tel:")
	kubun=input("kubun")
	up=input("sal up:")

	wst=Staff(ssn=ssn,fname=fname,lname=lname,bod=bod,address=address,tel=tel,kubun=kubun,sal=up)
	#wst.add_sal(int(up))
	
	print (wst)
	emplist.append([wst])
print (emplist)



filename='ch15-file'
with open(filename,'wb') as outf:
	pickle.dump(wst,outf)


filename='ch15-file'
load_emp(filename)
print (emplist)




for ii in range(len(emplist)):
	wemp=emplist[ii][0]
	
	
	print (wemp.lname,wemp.fname)
	
