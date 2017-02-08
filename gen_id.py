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


# class rand_id():

# 	def __init__(self):
# 		self.id = func_gen_id()

# 	def get_id(self):
# 		return self.id

print func_gen_id()