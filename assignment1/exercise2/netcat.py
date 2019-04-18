#!/usr/bin/env python3

import socket

port = 42424
host = "localhost"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
stringbuf = ""
for i in range(0, 1000):
    stringbuf = stringbuf + "spam " + str(i) + "\n"
buf = stringbuf.encode("utf-8")
s.sendto(buf, (host, port))
s.close()
