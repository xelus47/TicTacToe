#!/usr/bin/env python2

import sys, random, json
#from human import HumanPlayer
import display, human

class Observer():
	def __init__(self, name=""):
		self.name = "Observer"
		if name!="":
			self.name = name
		self.rand = __import__('random')
		self.ID = int(self.rand.getrandbits(32))


	def greet(self):
		return "Hello and good luck to both the players."
	def show(self, field):
		print field
		"""Give a reaction"""
		return random.choice("Nice|Well done|Oh|Interesting|Oh my...|I don't know anything|GG".split("|"))

class Player():
	"""Prototype class for players"""
	def __init__(self, name=""):
		self.name = "Randy"
		if name!="":
			self.name = name
		self.assigned = "?"
		self.rand = __import__('random')
		self.ID = int(self.rand.getrandbits(32)) # can be ignored
		
	def propose(self, problem):
		"""Return solution"""
		# place a stone at random
		problem=bytearray(problem)
		loop=True
		while loop:
			i=random.randrange(0, 9) # \in[0,8]
			if chr(problem[i])=='-':
				loop=False
				problem[i]=self.assigned
		return str(problem)


	def greet(self):
		return "gg hf"
	def celebrate(self):
		return "GG"
	def be_sad(self):
		return "gg wp"

def SeperatePlayers(field, emtpy="-"):
	field = bytearray(field)
	seperated={

	}
	for n in range(9):
		c=chr(field[n])
		if c!=emtpy:
			if c not in seperated:
				seperated[c]=bytearray("-"*9)
			seperated[c][n]=c
	for x in seperated:
		seperated[x]=str(seperated[x])
	return seperated

def GetFieldInfo(field):
	winning = [
		"s-- -s- --s",
		"--s -s- s--",
		"sss --- ---",
		"--- sss ---",
		"--- --- sss",
		"s-- s-- s--",
		"-s- -s- -s-",
		"--s --s --s"
	]

	info={'winner':'0','tied':False}

	seperate=SeperatePlayers(field)

	for w in seperate:
		#print w
		info[w]={}
		info[w]={'max':0,'average':0,'configs':[]}
		for k in range(len(winning)):
			condition=winning[k]
			status = condition.replace(" ","").replace("s",w)
			count=0
			for i in range(9):
				count=count+int(seperate[w][i]==status[i] and seperate[w][i]!='-')
			#print status, count
			info[w]['configs'].append({'config':status,'matches':count,'ID':k})
			info[w]['max']=max(info[w]['max'], count)
			info[w]['average']=info[w]['average']+1/8.0*count
			if count==3:
				info['winner']=w

	if info['winner']=='0' and field.count('-')==0:
		info['tied']=True

	return info


class Tictactoe():
	v=1.0
	def __init__(self,players): # players = array of Player() classes
		self.turn = random.randrange(0, 2) # 0 or 1
		self.players = players
		self.observers = []
		self.field = "-"*9

		self.players[0].assigned="X"
		self.players[1].assigned="O"

		self.introduction()

	def reset(self):
		self.field = "-"*9


	def introduction(self):
		print "Host: Welcome to Tictactoe v%s!"%self.v
		n=0
		for player in self.players:
			n=n+1
			print "Host: Player %s (%s) is assigned \"%s\""%(n, player.name, player.assigned)
			print "%s: \"%s\"" % (player.name, player.greet())
			print ""
		if len(self.observers)>0:
			print "Host: There are also %s special spectators that will observe and possibly comment on the game while it plays out."%len(self.observers)
			for observer in self.observers():
				print observer.name+": "+observer.greet()
			print ""

		print "Host: Player %s starts" %(self.turn+1)


	def play(self):
		self.field = self.players[self.turn].propose(self.field)
		for observer in self.observers:
			observer.show(self.field)

		info = GetFieldInfo(self.field)
		if info['winner']!="0":
			# TODO: notify spectators
			print "Host: Congratulations to %s for winning!"%self.players[self.turn].name
			print "%s: %s"%(self.players[self.turn].name, self.players[self.turn].celebrate())
			print "%s: %s"%(self.players[(self.turn+1)%2].name, self.players[(self.turn+1)%2].celebrate())
			print ""

			return
			

		elif info['tied']==True:
			# TODO: notify spectators
			print "Host: The match ended in a tie"
			print("")

			return

		else:
			self.turn=(self.turn+1)%2
			self.play()

	def quit(self):
		sys.exit(0)

if __name__=="__main__":
	game = Tictactoe([
		#human.HumanPlayer("Frisky"),
		Player(),
		Player()
		])

	game.observers.append(display.Displayer("Displayer"))

	winner= GetFieldInfo(game.field)['winner']
	while winner=='0':
		game.play()
		winner= GetFieldInfo(game.field)['winner']
		if winner!="0":
			print json.dumps(GetFieldInfo(game.field),indent=2)
		game.reset()


	sys.exit(0)
