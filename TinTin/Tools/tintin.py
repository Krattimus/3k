class TinTin(object):
	@staticmethod
	def execute(command, session="gts"):
		print("tintin_execute ({0}) {1}".format(session, command))

	@staticmethod
	def ticker(name, command, seconds, session="gts"):
		print("tintin_ticker ({0}) ({1}) ({2}) ({3})".format(session, name, command, seconds))

	@staticmethod
	def delay(name, command, seconds, session="gts"):
		print("tintin_delay ({0}) ({1}) ({2}) ({3})".format(session, name, command, seconds))

	@staticmethod
	def var(name, value, session="gts"):
		print("tintin_var ({0}) ({1}) ({2})".format(session, name, value))

	@staticmethod
	def send(command, session="gts"):
		print("tintin_send ({0}) {1}".format(session, command))

	@staticmethod
	def showme(command, session="gts"):
		print("tintin_showme ({0}) {1}".format(session, command))

	@staticmethod
	def echo(*args):
		if len(args) >= 2:
			session = args[-1]
			commands = ["({0})".format(command) for command in args[:-1]]
		else:
			session = "gts"
			commands = ["({0})".format(command) for command in args]
		commands = "{0}{1}".format(" ".join(commands), " ()" * (20-len(commands)))
		print("tintin_echo ({0}) {1}".format(session, commands))

