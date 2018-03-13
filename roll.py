#roll.py

from random import *


def identifyDiceTerm(term):
	if "d" in term:
		return True
	return False

def rolldice(params):

	values = []

	for param in params:
		if identifyDiceTerm(param):
			count = int(param.split('d')[0])
			sides = int(param.split('d')[1])

			times = count
			while times > 0:
				rollVal = randint(1, sides)
				values.append( (rollVal, "D") )
				times-=1
		else:
			if "+" not in param:
				values.append( (int(param), "C" ) )

	return formatRoll(values)

def formatRoll(values):
	output = "```\n"
	rollsum = 0

	i = 0
	while i < len(values):
		value = values[i]
		if value[1] == "D":
			output += "[" + str(value[0]) + "]"
		else:
			output += str(value[0])
		if i < len(values) - 1:
			output += " + "
		else:
			output += " = "
		rollsum += value[0]
		i+=1
	output += str(rollsum) + "```"
	# print (output)
	return output




	# #handle params
	# die = params[0]
	# count = int(die.split('d')[0])
	# sides = int(die.split('d')[1])

	# constants = []
	# raw_constants = params[1:]
	# if len(raw_constants) > 0:
	# 	#clean constants and convert to int
	# 	i = 1
	# 	while i < len(raw_constants):
	# 		constants.append(int(raw_constants[i]))
	# 		i += 2
	# 	# constants.sum = sum(constants)

	# #do the actual rolling
	# times = count
	# while times > 0:
	# 	values.append( randint(1, sides) )
	# 	times -= 1

	# print(str(values))
	# if len(constants) == 0:
	# 	return formatDiceOutputOld(values)
	# else:
	# 	return formatDiceOutputOld(values, constants)



# def formatDiceOutputOld(values, constants=None):
# 	output = "```\n"
# 	valsum = 0
# 	i = 0
# 	while i < len(values):
# 		val = values[i]
# 		output += "[" + str(val) + "]"
# 		if i < len(values) - 1:
# 			output += ' + '

# 		valsum += val
# 		i += 1

# 	if constants is not None:
# 		output += ' + '
# 		i = 0
# 		while i < len(constants):
# 			val = constants[i]
# 			output += str(val)
# 			if i < len(constants) - 1:
# 				output += ' + '
# 			valsum += val
# 			i += 1

# 	output += ' = ' + str(valsum)
# 	output += '\n```'
# 	return output


# class dice:
# 	def __init__(self, sides, count, constants = []):
# 		self.sides = int(sides)
# 		self.count = int(count)
# 		self.values = []
# 		for i in constants:
# 			i = int(i)
# 		self.constants = constants

# 	def roll(self):
# 		self.values = []

# 		times = self.count
# 		while times > 0:
# 			self.values.append( randint(1, self.sides) )
# 			times-=1
# 		print(self.values)

# 	def sum(self):
# 		sum = 0
# 		for i in values:
# 			sum += i
# 		for i in constants:
# 			sum += constants
# 		return sum