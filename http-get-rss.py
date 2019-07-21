#!/bin/bash
import socket
import re

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect( ('greens.org', 80) )

cmd = 'GET http://www.greens.org/about/software/editor.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    text = data.decode()
    for line in text:
        if re.search('title', text, re.S):
            print(line, end='')
                
my_socket.close()
print("Done. Exiting...")