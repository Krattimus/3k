class TinTin(object):
	@staticmethod
	def execute(command):
		print("{0}".format(command))

	@staticmethod
	def ticker(name, command, seconds):
		print("#ticker {0} {1} {2}".format(name, command, seconds))

	@staticmethod
	def delay(name, command, seconds):
		print("#delay {{{0}}} {{{1}}} {{{2}}}".format(name, command, seconds))

	@staticmethod
	def var(name, value):
		print("#var {0} {1}".format(name, value))

	@staticmethod
	def send(command):
		print("#send {0}".format(command))

	@staticmethod
	def showme(command):
		print("#showme {0}".format(command))

	@staticmethod
	def echo(args):
		print("#echo {0}".format(args))

