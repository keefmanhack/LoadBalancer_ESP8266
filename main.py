# while True:
  # print('Got a connection from %s' % str(addr))
  # request = conn.recv(1024) #return value is a byte object representing data received, argument is max size of data that can be received at once
  # request = str(request)
  # # print('Content = %s' % request)

  # response = """<h1>"""+str(ct)+"""</h1> """
  # ct=ct+1
  # conn.send('HTTP/1.1 200 OK\n')
  # conn.send('Content-Type: text/html\n')
  # conn.send('Connection: close\n\n')
  # conn.sendall(response)
  # conn.close()
