#!/usr/bin/env python3

import socket


# handle is not used anymore for UDP
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


# we still use handledatastring to make sure that the data is filtered in the sameway as exercise 1
def handledatastring(datastring: str, length: int, delimiter):
	stringlist = datastring.split(sep=delimiter)
	filteredlist = []
	for string in stringlist:
		filteredlist.append(string[length:])
	filteredlist = delimiter.join(filteredlist)
	return filteredlist


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	data, addr = s.recvfrom(size)
	print(handledatastring(data.decode("utf-8"), len("spam "), "\n"))

if __name__ == '__main__':
	host = "localhost"
	port = 42424
	size = 65535
	main()
