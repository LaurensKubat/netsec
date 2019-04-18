#!/usr/bin/env python3

import socket

port = 42424
host = "localhost"

s = socket.create_connection((host, port))
stringbuf = ""
for i in range(0, 1000):
    stringbuf = stringbuf + "spam " + str(i) + "\n"
buf = stringbuf.encode("utf-8")
s.sendall(buf)
s.close()
