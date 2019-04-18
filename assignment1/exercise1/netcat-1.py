#!/usr/bin/env python3

import socket


def handle(passedconn):
	data = b""
	newdata = passedconn.recv(size)
	while newdata:
		data += newdata
		newdata = passedconn.recv(size)
	if data:
		datastring = data.decode("utf-8")
		print(handledatastring(datastring, len("spam "), "\n"))
	passedconn.close()


def handledatastring(datastring: str, length: int, delimiter):
	stringlist = datastring.split(sep=delimiter)
	filteredlist = []
	for string in stringlist:
		filteredlist.append(string[length:])
	filteredlist = delimiter.join(filteredlist)
	return filteredlist


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(backlog)
	for i in [1, 2, 3]:
		conn, clientaddress = s.accept()
		handle(passedconn=conn)
	s.close()

if __name__ == '__main__':
	host = "localhost"
	port = 42424
	backlog = 5
	size = 1024
	main()
