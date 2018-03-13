#commandParser.py

class Parse:

	def __init__(self, raw_in):
		self.intake = raw_in.split()
		self.command = self.intake[0]
		self.params = self.intake[1:]
		print("Command: ", self.cmd)
		print("Params: ", str(self.params))

