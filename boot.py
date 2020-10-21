import uasyncio
import network
import esp
import gc
import json
from src.RequestReceiver import RequestReceiver
from src.load_balancer import LoadBalancer


#get configuration data
with open("config.json", 'r') as f:
	configData = json.load(f)


esp.osdebug(None)
gc.collect()


ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid=configData["network_config"]["name"]) # set the ESSID of the access point
ap.config(password=configData["network_config"]["password"])
ap.ifconfig(configData["network_config"]["config"])

ap.active(True)         # activate the interface

print('\n\n\n\n\n')
print(configData)
print(ap.ifconfig())

print('\n\n\n\n\n')

reqRec = RequestReceiver(configData["max_queue_size"])
loadBal = LoadBalancer(configData["servers"], configData["balance_method"])

ct=0;
while True:
	req = reqRec.getRequest()
	if(req != False):
		server = loadBal.getServer()
		print(server)

		conn, addr = req
		conn.send('HTTP/1.1 200 OK\n')
		conn.send('Content-Type: text/html\n')
		conn.send('Connection: close\n\n')
		conn.sendall("""<h1>request number: """ + str(ct) + """</h1>""")
		ct=ct+1
		conn.close()