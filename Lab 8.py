#Lab8
#Instructor Olac Fuentes
#5/14/19
import random
import mpmath
Start =time.time()
#the methods below test the functions 
def sin()
	#repeat a 1000 tiems
	for i in range (100):
		#generate random numbers
		t=random.randrange(-3.14,3.14)
		#get value to compare
		A=sin(t)-cos(t)
		#if = 0 or close enough it is true otherwise false
		if A>=.00001 or A<= -.00001:
			return False
	return true
def sec()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
def tan()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
def Nsin()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
def Nsec()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
def Ntan()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
	def cos()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
	def Ncos()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
	def sincos()
	for i in range (100):
		t=random.randrange(-3.14,3.14)
		A=cos(t) - sin(t)
		if A>=.00001 or A<= -.00001:
			return False
	return true
def partion(S):
	count=0
	count2=0
	for j in range (len(S)):
		A=S[j]
		for i in range (len(S)):
			if S[i]== A:
			    print("S1 =",[S[i],"S2 =",S[i])
				return True
	print("NO SUCH PARTION EXISTS")
	return False