#!usr/bin/Python
import time
import random
import math

def func_gen_id(): #Function to gene
	lists = [["d","e","f","g"], ["m","n","o","p"],["q","r","s","t"]]
	id_ = str(random.random()*time.time())[1:5]
	al = lists[int(math.floor(random.random()*3))][int(math.floor(random.random()*4))]
	al2 = lists[int(math.floor(random.random()*3))][int(math.floor(random.random()*4))]
	al3 = lists[int(math.floor(random.random()*3))][int(math.floor(random.random()*4))]
	al4 = lists[int(math.floor(random.random()*3))][int(math.floor(random.random()*4))]

	id_ = al + al3 + id_ + al4 + al2
	del al, al2, al3, al4, lists
	return id_


class get_id():

	def __init__(self):
		self.id = func_gen_id()

	def get8(self):
		return self.id

	def get12(self):
		fix12 = lambda x : x + func_gen_id()[3] + func_gen_id()[int(math.floor(random.random()*4))] + func_gen_id()[-1] + func_gen_id()[1]
		return fix12(self.id)

	def get16(self):
		fix16 = lambda x : x + func_gen_id()[4] + func_gen_id()[int(math.floor(random.random()*4))] + func_gen_id()[-1] + func_gen_id()[1]
		return fix16(self.get12())