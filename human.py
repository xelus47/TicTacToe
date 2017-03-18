#!/usr/bin/env python2

import display

class Player():
	"""Prototype class for players"""
	def __init__(self, name=""):
		self.assigned = "?"
		self.rand = __import__('random')
		self.name = name
		self.ID = int(self.rand.getrandbits(32)) # can be ignored

		if self.name=="":
			self.name=raw_input("HumanPlayer: Choose your name: "%self.ID)
		
	def propose(self, problem):
		"""Return solution"""
		# place a stone at random
		problem=bytearray(problem)
		loop=True
		while True:
			i=random.randrange(0, 9) # \in[0,8]
			if chr(problem[i])=='-':
				loop=False
				problem[i]=self.assigned
		return str(problem)


	def greet(self):
		return raw_input("%s (greet): "%self.name)
	def celebrate(self):
		return raw_input("%s (you win): "%self.name)
	def be_sad(self):
		return raw_input("%s (you lose): "%self.name)


class HumanPlayer(Player):
	def propose(self, problem):
		print display.showField(problem, True)

		problem = bytearray(problem)
		while True:
			b=int(raw_input("Input: "))-1
			if chr(problem[b])=='-':
				problem[b]=self.assigned
				break
		return str(problem)
