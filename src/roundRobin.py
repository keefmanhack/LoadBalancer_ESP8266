class RoundRobin:
	def __init__(self, servers):
		self.servers = servers;
		self.index = len(servers)-1;

	def getServer(self):
		if(self.index <0):
			return
		self.index = (self.index +1) % len(self.servers)
		return self.servers[self.index]