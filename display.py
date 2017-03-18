from game import Observer

def showField(field, numbered=False):
	
	board = ' a | b | c \n'
	board+= '---+---+---\n'
	board+= ' d | e | f \n'
	board+= '---+---+---\n'
	board+= ' g | h | i \n'

	alfa = 'abcdefghi'
	for n in range(9):
		c=field[n]
		if numbered:
			if c!='-':
				board=board.replace(alfa[n],' ')
			else:
				board=board.replace(alfa[n],str(n+1))
		else:
			if c!='-':
				board=board.replace(alfa[n],c)
			else:
				board=board.replace(alfa[n],' ')
	
	return board

class Displayer(Observer):
	def show(self,field):
		print showField(field)


# 185 953 1971, 100 539 372, 274 486 387 313 