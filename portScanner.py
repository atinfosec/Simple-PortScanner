#!/usr/bin/env python3

import argparse
import socket

def sockConnect(ip,port):
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		try:
			s.connect((ip,port))
		except:
			
			print('No connection established for {}:{}'.format(ip,port))
		
		try:
			s.send(b'testing\r\n')
			result = s.recv(1024)
			print(result.decode())
		except:	
			print('[-] Something went wrong \n')
		

def resolveHost(hostList,portList):
	#this funtion resolve hostname to address and call function to connect to port
	ips = []
	try:
		for i in hostList:
			address = socket.gethostbyname(i)
			ips.append(address)
	
	except:
		print('Unable to resolve host')
	
	for ip in ips:
		for port in portList:
			print('[+] Checking for {}:{}........'.format(ip,port))
			sockConnect(ip,port)
			

def main():
	parser = argparse.ArgumentParser(description='A Simple port scanner')
	parser.add_argument('host',help='Host to scan, if multiple host then type all separated by comma')
	parser.add_argument('-p','--ports',help='ports to scan, if multiple ports then comma separate them')
	args = parser.parse_args()

	hosts = args.host.split(',')

	if args.ports:
		strPorts = args.ports.split(',') #list of ports have string type
		ports = [int(i) for i in strPorts] #converting list of string ports in int type
	else:
		ports = [1,2,3,4,5] #if user do not provide ports flag then default ports to scan
	
	resolveHost(hosts,ports)
	#Now both IP and ports have list type


if __name__ == '__main__':
	main()
