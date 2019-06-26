# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent

class MyAI ( Agent ):

	def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
		self._current_board = dict()
		self._x = 0
		self._y = 0
		self._direction = 2
		self._add_value = ""
		self._turn_around = False
		self._backtrace = False
		self._been_everywhere = False
		self._gold = False
		self._count = 0
		self._list_count = 0
		self._list = []
		self._master_list = []
		#pass
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

	def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        
		#print(self._list)
		#print(self._x, self._y)
		#print(self._master_list)


		if (self._gold and len(self._master_list) == 0):
			return Agent.Action.CLIMB
		#print(self._master_list)

		if (self._gold and self._x == 0 and self._y == 0):
			return Agent.Action.CLIMB

		if (self._x == 0 and self._y == 0):
			if (self._direction == 4 or self._direction == 3):
				return Agent.Action.CLIMB

		if (glitter):
			#print("FOUND GOLD")
			self._gold = True
			self._turn_around = True
			return Agent.Action.GRAB

		if (self._turn_around):
			#print("turning around...")
			#print("direction before", self._direction)
			if (self._count < 2):
				#print("bruh")
				self._count+=1
				self.update_direction(1)
				#print("direction after", self._direction)
				if (not self._gold):
					#print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
					#self._list.append(Agent.Action.TURN_RIGHT)
					self._master_list.append(Agent.Action.TURN_RIGHT)#######
				return Agent.Action.TURN_LEFT
			else:
				#print("done turning.")
				#print("direction final", self._direction)
				self._turn_around = False
				self._count = 0
				#return


		if (self._gold):
			#print(self._master_list)
			#print("FOUND GOLD GOING HOME")
			#print(self._x, self._y)
			if (bump):
				#del self._master_list[-1]
				if (self._direction == 1):
					self._y -= 1
				if (self._direction == 2):
					self._x -= 1
				if (self._direction == 3):
					self._y += 1
				if (self._direction == 4):
					self._x += 1

			next_move = self._master_list[-1]
			del self._master_list[-1]
			if (next_move == Agent.Action.TURN_LEFT):
				self.update_direction(1)
			if (next_move == Agent.Action.TURN_RIGHT):
				self.update_direction(2)
			if (next_move == Agent.Action.FORWARD):
				#print("moving forward because of gold")
				self.update_location()
			return next_move


		if (self._backtrace):
			if (self._x == 0 and self._y == 0):
				return Agent.Action.CLIMB
			#if (breeze or stench):#(can go):
			
			if (bump):
				del self._list[-1]
				del self._master_list[-1]
				self._current_board[str(self._x)+str(self._y)] = "bump"

				if (self._direction == 1):
					self._y -= 1
				elif (self._direction == 2):
					self._x -= 1
				elif (self._direction == 3):
					self._y += 1
				elif (self._direction == 4):
					self._x += 1				

				self._turn_around = True
				#return 0
			else:
				if (str(self._x)+str(self._y) not in self._current_board):
					self._current_board[str(self._x)+str(self._y)] = ""
					self._list.append(Agent.Action.FORWARD)
					#if (not self._gold):
					#self._master_list.append(Agent.Action.FORWARD)
					self._backtrace = False
					return 0
			
			if (breeze or stench or self._been_everywhere):
				#print(self._list)
				new_move = self._list[-1]
				self._master_list.append(new_move)
				del self._list[-1]
				if (new_move == Agent.Action.TURN_LEFT):
					self.update_direction(1)
					#self._list.append(Agent.Action.TURN_LEFT)
					#self._master_list.append(Agent.Action.TURN_LEFT)
				if (new_move == Agent.Action.TURN_RIGHT):
					self.update_direction(2)
					#self._list.append(Agent.Action.TURN_RIGHT)
					#self._master_list.append(Agent.Action.TURN_RIGHT)
				if (new_move == Agent.Action.FORWARD):
					self._been_everywhere = False
					self.update_location()
					#self._list.append(Agent.Action.FORWARD)
					#print("moving forward because of backtrace")
					#self._master_list.append(Agent.Action.FORWARD)
				return new_move
			

			if (str(self._x+1) + str(self._y) not in self._current_board):
				if (self._direction != 2):
					self.update_direction(1)
					#self._list.append(Agent.Action.TURN_RIGHT)
					self._master_list.append(Agent.Action.TURN_RIGHT)
					return Agent.Action.TURN_LEFT
				else:
					self.update_location()
					#self._list.append(Agent.Action.FORWARD)
					self._master_list.append(Agent.Action.FORWARD)
					#print("right backtrace forward")
					return Agent.Action.FORWARD
			elif (str(self._x) + str(self._y+1) not in self._current_board):
				if (self._direction != 1):
					self.update_direction(1)
					#self._list.append(Agent.Action.TURN_RIGHT)
					self._master_list.append(Agent.Action.TURN_RIGHT)
					return Agent.Action.TURN_LEFT
				else:
					self.update_location()
					#self._list.append(Agent.Action.FORWARD)
					self._master_list.append(Agent.Action.FORWARD)
					#print("up backtrace forward")
					return Agent.Action.FORWARD
			elif (str(self._x-1) + str(self._y) not in self._current_board):
				if (self._direction != 4):
					self.update_direction(1)
					#self._list.append(Agent.Action.TURN_RIGHT)
					self._master_list.append(Agent.Action.TURN_RIGHT)
					return Agent.Action.TURN_LEFT
				else:
					self.update_location()
					#self._list.append(Agent.Action.FORWARD)
					self._master_list.append(Agent.Action.FORWARD)
					#print("left backtrace forward")
					return Agent.Action.FORWARD
			elif (str(self._x) + str(self._y-1) not in self._current_board):
				if (self._direction != 3):
					self.update_direction(1)
					#self._list.append(Agent.Action.TURN_RIGHT)
					self._master_list.append(Agent.Action.TURN_RIGHT)
					return Agent.Action.TURN_LEFT
				else:
					self.update_location()
					#self._list.append(Agent.Action.FORWARD)
					self._master_list.append(Agent.Action.FORWARD)
					#print("down backtrace forward")
					return Agent.Action.FORWARD
			else:
				self._been_everywhere = True
				return 0

			


		if (self._x == 0 and self._y == 0):
			if (breeze or stench):
				return Agent.Action.CLIMB
		
		if (bump):
			if (self._direction == 1):
				self._y -= 1
			if (self._direction == 2):
				self._x -= 1
			if (self._direction == 3):
				self._y += 1
			if (self._direction == 4):
				self._x += 1


			self.update_direction(1)
			self._list.append(Agent.Action.TURN_RIGHT)
			self._master_list.append(Agent.Action.TURN_RIGHT)
			return Agent.Action.TURN_LEFT

		if (not self._backtrace):
			if (not breeze):
				if (not stench):
					self.update_location()
					self._list.append(Agent.Action.FORWARD)
					self._master_list.append(Agent.Action.FORWARD)
					#print("REGULAR FORWARD")
					'''
					if (breeze):
						self._add_value += "b"
					if (stench):
						self._add_value += "s"
					if (str(self._x)+str(self._y)in self._current_board):
						#print("current location already in dict")
						pass
					else:
						#print("ADDING TO DICT")
						self._current_board[str(self._x) + str(self._y)] = self._add_value

					'''
					return Agent.Action.FORWARD

		
		if (breeze):
			self._add_value += "b"
		if (stench):
			self._add_value += "s"
		if (str(self._x)+str(self._y) in self._current_board):
			pass
		else:
			self._current_board[str(self._x)+str(self._y)] = self._add_value

		
		if (breeze or stench):
			if (not self._backtrace):
				self._turn_around = True
				self._backtrace = True
				return 0
			else:
				#self._list_count = len(self._list)-1
				pass
				#return self._list[-1]#decode and update dir or loc!

		#return Agent.Action.CLIMB
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

	def update_location(self):
		if (self._direction == 1):
			self._y += 1
		if (self._direction == 2):
			self._x += 1
		if (self._direction == 3):
			self._y -= 1
		if (self._direction == 4):
			self._x -= 1

	def update_direction(self, dir):
		if (dir == 1):
			if (self._direction == 1):
				self._direction = 4
			elif (self._direction == 2):
				self._direction = 1
			elif (self._direction == 3):
				self._direction = 2
			elif (self._direction == 4):
				self._direction = 3
		if (dir == 2):
			if (self._direction == 1):
				self._direction = 2
			elif (self._direction == 2):
				self._direction = 3
			elif (self._direction == 3):
				self._direction = 4
			elif (self._direction == 4):
				self._direction = 1

	def adj_check(self, x, y):
		return_values = ""
		a = str(x+1)+str(y)
		b = str(x)+str(y+1)
		c = str(x-1)+str(y)
		d = str(x)+str(y-1)		

		if (a in self._current_board):
			return_values += self._current_board[a]
		if (b in self._current_board):
			return_values += self._current_board[b]
		if (c in self._current_board):
			return_values += self._current_board[c]
		if (d in self._current_board):
			return_values += self._current_board[d]

		return return_values

    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
