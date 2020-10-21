from .queue import Queue
try:
  import usocket as socket
except:
  import socket

class RequestReceiver(): 
    # constructor 
    def __init__(self, size): # initializing the class 
        self.size = size
        self.q = Queue(self.size)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #sock_stream defines usage for TCP/IP #AF_INET defines a host IP, port as tuple
        self.s.bind(('', 80)) #socket can accept from any host on port 80
        self.s.listen(5) #number of connections system will allow before refusing new connetions
        self.s.setsockopt(socket.SOL_SOCKET, 20, self.my_event_handler)
        self.ct =0

    def my_event_handler(self, socket):
        print('Request Received')
        conn, addr = self.s.accept()
        self.q.enqueue((conn, addr))

    def getRequest(self):
        return self.q.dequeue()
