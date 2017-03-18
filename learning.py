#!/usr/bin/env python2

import display
from game import *


class ObserverBot(Player): # observes previous games and decides which patterns are winning patterns and plays not to lose
	pass

class DisrespectBot(Player): # will not play the best move possible if it thinks the opponent made a mistake
	pass

class GhandiBot(Player): # neither wants to win nor lose
	pass

class MemeMaxBot(Player): # minimax principle
	depth = 1 # full
	def setdepth(self, n):
		if n is int:
			self.depth=9
			return self.depth
		else:
			return 0
	def propose(self, problem):

		symbols=['X','O']
		while symbols[0]!=self.assigned:
			a=symbols.pop(0)
			symbols=symbols.append(a)

		tree=[
			
		]

		i=0
		while i<self.depth:
			for k in range(9):
				if problem[k]=='-':
					tmpBoard = bytearray(problem)
					#tmpBoard[k]=


class TrololoBot(MemeMaxBot): # shallow (depth=1) minimax
	depth = 1


if __name__=='__main__':
	symbols=['X','O']
	while symbols.__getitem__(0)!='O':
		a=symbols.pop(0)
		print a
		symbols=symbols.append(a)

	print symbols