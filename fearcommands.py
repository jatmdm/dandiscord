#fearcommands.py
import discord
from roll import *
from random import *
import io

class FearCommands:

	def helpcommand(self):
		helptxt = open('fear/help.txt', 'r')
		ret = helptxt.read()
		return ret

	def mecommand(self, params):

		if len(params) != 1:
			return "I can't greet them..."

		author = params[0]

		greetings = open('fear/greetings.txt', 'r')
		greetings = greetings.readlines()
		# print(greetings)
		greeting = greetings[randint(0, len(greetings)-1)]


		greeting = greeting.replace("{name}", author)


		# print(greeting)
		return greeting

	def __init__(self):
		self.commands = dict()
		self.commands.update( {"!roll" : rolldice } )
		self.commands.update( {"!greet" : self.mecommand } )
		self.commands.update( {"!help" : self.helpcommand } )
		print("#### FearCommands LOADED ####")

FearCommands = FearCommands()