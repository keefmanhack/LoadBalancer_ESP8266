from .roundRobin import RoundRobin

class LoadBalancer(): 
    # constructor 
    def __init__(self, serverData, balanceMethodStr): # initializing the class 
        if(balanceMethodStr=="round robin"):
            self.balanceMethod = RoundRobin(serverData)

        
    def getServer(self):
        return self.balanceMethod.getServer()



