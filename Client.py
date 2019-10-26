import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9008))
data=s.recv(1000)
data=str(data, 'utf-8')
print(data)
while data!='no':
	p=input('Cosa vuoi dire?')
	s.send(bytes(p,'utf-8'))
	data=s.recv(1000)
	data=str(data, 'utf-8')
	if data == 'chiudi':
		break
	print(data)
s.close()
