#!/usr/bin/python
# -*- coding: utf-8 -*-
import psutil
from time import sleep
from commands import getstatusoutput
import os

adapterName = 'Conexao de Rede sem Fio'
SecundaryAdapterName = 'Conexao de Rede sem Fio 2'
metric=1
speed_limit = 300
s = os.system('netsh interface ipv4 set interface "%s" metric=%d' %(adapterName, metric))
print s
s = os.system('netsh interface ipv4 set interface "%s" metric=%d' %(SecundaryAdapterName, 25))
print s
while(True):
	networkData = psutil.network_io_counters(pernic=True)
	initial_bytes_sent = networkData[adapterName][0]
	initial_bytes_recv = networkData[adapterName][1]
	sleep(1)
	networkData = psutil.network_io_counters(pernic=True)
	bytes_sent = networkData[adapterName][0]
	bytes_recv = networkData[adapterName][1]

	diff_sent = bytes_sent - initial_bytes_sent
	diff_recv = bytes_recv - initial_bytes_recv

	speed = diff_recv/1024
	print '%d KB/s' % speed  
	
	if speed > speed_limit:
		print 'Passou limite da rede'
		if metric == 50:
			pass
		else:
			metric = 50
			s = os.system('netsh interface ipv4 set interface "%s" metric=%d' %(adapterName, metric))
			print s
	else:
		print 'Dentro do limite'
		if metric == 1:
			pass
		else:
			metric = 1
			s = os.system('netsh interface ipv4 set interface "%s" metric=%d' %(adapterName, metric))
			print s
			

	