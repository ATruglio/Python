import socket


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9008))
s.listen(5)
while True:
	c,a=s.accept()
	c.send(bytes('OK','utf-8'))
	data = c.recv(1000)
	data=str(data, 'utf-8')
	print('client says:', data)
	while data!='no':
		if data =='ciao come stai?':
			c.send(bytes('Tutto bene','utf-8'))
		else :
			c.send(bytes('Hai qualcosa da dirmi?','utf-8'))
		c.send(bytes('Se vuoi terminare la chat iserisci: no','utf-8'))
		data = c.recv(1000)
		data=str(data, 'utf-8')

	c.send(bytes('chiudi','utf-8'))
	print('chiusura connessione')
	c.close()
